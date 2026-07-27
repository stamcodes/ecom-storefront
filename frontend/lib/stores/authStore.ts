import { create } from "zustand";
import { persist } from "zustand/middleware";
import * as authApi from "@/lib/api/auth";
import { CustomerProfile } from "@/types/user";
import { LoginSchemaType, RegisterSchemaType } from "@/lib/validation/auth";

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  user: CustomerProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;

  login: (credentials: LoginSchemaType) => Promise<void>;
  register: (data: RegisterSchemaType) => Promise<void>;
  logout: () => Promise<void>;
  refreshAccessToken: () => Promise<string>;
  setUser: (user: CustomerProfile) => void;
  clearAuth: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      accessToken: null,
      refreshToken: null,
      user: null,
      isAuthenticated: false,
      isLoading: false,

      login: async (credentials) => {
        set({ isLoading: true });
        try {
          const token = await authApi.login(credentials);
          set({
            accessToken: token.accessToken,
            refreshToken: token.refreshToken,
            isAuthenticated: true,
            isLoading: false,
          });
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      register: async (data) => {
        set({ isLoading: true });
        try {
          await authApi.register(data);
          // Backend does NOT return a token on register — email verification required first.
          // No auto-login here; caller should redirect to a "check your email" screen.
          set({ isLoading: false });
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      logout: async () => {
        const { refreshToken } = get();
        if (refreshToken) {
          try {
            await authApi.logout(refreshToken);
          } catch {
            // Ignore failures — clear local state regardless.
          }
        }
        get().clearAuth();
      },

      refreshAccessToken: async () => {
        const { refreshToken } = get();
        if (!refreshToken) {
          get().clearAuth();
          throw new Error("No refresh token available");
        }
        try {
          const token = await authApi.refreshToken(refreshToken);
          set({
            accessToken: token.accessToken,
            refreshToken: token.refreshToken, // rotated on backend
            isAuthenticated: true,
          });
          return token.accessToken;
        } catch (error) {
          get().clearAuth();
          throw error;
        }
      },

      setUser: (user) => set({ user }),

      clearAuth: () =>
        set({
          accessToken: null,
          refreshToken: null,
          user: null,
          isAuthenticated: false,
        }),
    }),
    {
      name: "auth-storage",
      partialize: (state) => ({
        accessToken: state.accessToken,
        refreshToken: state.refreshToken,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
