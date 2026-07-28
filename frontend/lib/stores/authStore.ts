import { create } from "zustand";
import * as authApi from "@/lib/api/auth";
import { CustomerProfile } from "@/types/user";
import { LoginSchemaType, RegisterSchemaType } from "@/lib/validation/auth";

interface AuthState {
  user: CustomerProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  isInitialized: boolean;

  login: (credentials: LoginSchemaType) => Promise<void>;
  register: (data: RegisterSchemaType) => Promise<void>;
  logout: () => Promise<void>;
  fetchCurrentUser: () => Promise<void>;
  setUser: (user: CustomerProfile) => void;
  clearAuth: () => void;
}

function clearClientCookies() {
  if (typeof document !== "undefined") {
    const cookiesToClear = ["access_token", "refresh_token", "session", "token"];
    const paths = ["/", "/account", "/api"];
    const hostname = window.location.hostname;
    const domains = [hostname, "." + hostname];

    cookiesToClear.forEach((name) => {
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
      paths.forEach((path) => {
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=${path};`;
        domains.forEach((domain) => {
          document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=${path}; domain=${domain};`;
        });
      });
    });
  }
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  isInitialized: false,

  login: async (credentials: LoginSchemaType) => {
    set({ isLoading: true });
    try {
      await authApi.login(credentials);
      const user = await authApi.getCurrentUser();
      set({ user, isAuthenticated: true, isLoading: false, isInitialized: true });
    } catch (error) {
      set({ isLoading: false });
      throw error;
    }
  },

  register: async (data: RegisterSchemaType) => {
    set({ isLoading: true });
    try {
      await authApi.register(data);
      set({ isLoading: false });
    } catch (error) {
      set({ isLoading: false });
      throw error;
    }
  },

  logout: async () => {
    try {
      await authApi.logout();
    } catch {
      // Ignore failures — clear local state regardless.
    }
    clearClientCookies();
    if (typeof window !== "undefined") {
      localStorage.clear();
      sessionStorage.clear();
    }
    set({ user: null, isAuthenticated: false, isInitialized: true });
  },

  fetchCurrentUser: async () => {
    set({ isLoading: true });
    try {
      const user = await authApi.getCurrentUser();
      set({ user, isAuthenticated: true, isLoading: false, isInitialized: true });
    } catch {
      set({ user: null, isAuthenticated: false, isLoading: false, isInitialized: true });
    }
  },

  setUser: (user: CustomerProfile) => set({ user }),

  clearAuth: () => {
    clearClientCookies();
    if (typeof window !== "undefined") {
      localStorage.clear();
      sessionStorage.clear();
    }
    set({ user: null, isAuthenticated: false, isInitialized: true });
  },
}));
