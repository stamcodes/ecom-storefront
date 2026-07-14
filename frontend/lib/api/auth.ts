import { apiClient, ApiError } from "./client";
import { ApiResponse, AuthResponseData } from "@/types/api";
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

export async function login(
  credentials: LoginSchemaType,
  signal?: AbortSignal
): Promise<ApiResponse<AuthResponseData>> {
  try {
    return await apiClient.post<ApiResponse<AuthResponseData>>("/auth/login", credentials, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.login);
  }
}

export async function register(
  userData: RegisterSchemaType,
  signal?: AbortSignal
): Promise<ApiResponse<AuthResponseData>> {
  try {
    return await apiClient.post<ApiResponse<AuthResponseData>>("/auth/register", userData, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.register);
  }
}

export async function refreshToken(
  signal?: AbortSignal
): Promise<ApiResponse<{ accessToken: string }>> {
  try {
    return await apiClient.post<ApiResponse<{ accessToken: string }>>("/auth/refresh", undefined, {
      signal,
      skipAuthRetry: true,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

export async function logout(signal?: AbortSignal): Promise<ApiResponse<null>> {
  try {
    return await apiClient.post<ApiResponse<null>>("/auth/logout", undefined, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.logout);
  }
}

export async function forgotPassword(
  data: ForgotPasswordSchemaType,
  signal?: AbortSignal
): Promise<ApiResponse<null>> {
  try {
    return await apiClient.post<ApiResponse<null>>("/auth/forgot-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.forgotPassword);
  }
}

export async function resetPassword(
  data: ResetPasswordSchemaType,
  signal?: AbortSignal
): Promise<ApiResponse<null>> {
  try {
    return await apiClient.post<ApiResponse<null>>("/auth/reset-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resetPassword);
  }
}

export async function verifyEmail(token: string, signal?: AbortSignal): Promise<ApiResponse<null>> {
  try {
    return await apiClient.post<ApiResponse<null>>("/auth/verify-email", { token }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.verifyEmail);
  }
}
