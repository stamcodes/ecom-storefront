import { apiClient, ApiError } from "./client";
import { CustomerProfile } from "@/types/user";
import {
  LoginSchemaType,
  RegisterSchemaType,
  ResetPasswordSchemaType,
  ForgotPasswordSchemaType,
} from "@/lib/validation/auth";

const FALLBACK_MESSAGES = {
  login: "We couldn't sign you in. Please check your credentials and try again.",
  register: "We couldn't create your account. Please try again.",
  refresh: "Your session has expired. Please log in again.",
  logout: "We couldn't log you out. Please try again.",
  forgotPassword: "We couldn't send the password reset email. Please try again.",
  resetPassword: "We couldn't reset your password. Please try again.",
  verifyEmail: "We couldn't verify your email. Please try again.",
  resendVerification: "We couldn't resend the verification email. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

// POST /customer/auth/register — returns id/name/email/emailVerified/message, NOT a token
export async function register(
  userData: RegisterSchemaType,
  signal?: AbortSignal
): Promise<{ id: number; name: string; email: string; emailVerified: boolean; message: string }> {
  try {
    return await apiClient.post("/customer/auth/register", userData, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.register);
  }
}

// POST /customer/auth/login
export async function login(
  credentials: LoginSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post<{ message: string }>("/customer/auth/login", credentials, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.login);
  }
}

// POST /customer/auth/refresh
export async function refreshToken(signal?: AbortSignal): Promise<{ message: string }> {
  try {
    return await apiClient.post<{ message: string }>(
      "/customer/auth/refresh",
      {},
      { signal, skipAuthRetry: true }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

// POST /customer/auth/logout
export async function logout(signal?: AbortSignal): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/logout", {}, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.logout);
  }
}

export async function getCurrentUser(signal?: AbortSignal): Promise<CustomerProfile> {
  try {
    const response = await apiClient.get<{
      id: number;
      name: string;
      email: string;
      phone_number: string | null;
      avatar_url: string | null;
      email_verified: boolean;
      created_at: string;
    }>("/customer/auth/me", { signal });

    return {
      id: response.id,
      name: response.name,
      email: response.email,
      phoneNumber: response.phone_number,
      avatarUrl: response.avatar_url,
      emailVerified: response.email_verified,
      createdAt: response.created_at,
    };
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

// POST /customer/auth/verify-email
export async function verifyEmail(
  token: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/verify-email", { token }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.verifyEmail);
  }
}

// POST /customer/auth/resend-verification
export async function resendVerification(
  email: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/resend-verification", { email }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resendVerification);
  }
}

// POST /customer/auth/forgot-password
export async function forgotPassword(
  data: ForgotPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/forgot-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.forgotPassword);
  }
}

// POST /customer/auth/reset-password
export async function resetPassword(
  data: ResetPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/reset-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resetPassword);
  }
}
