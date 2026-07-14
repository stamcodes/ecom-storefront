import { ApiErrorResponse } from "@/types/api";

export type ApiErrorType = "http" | "parse" | "network" | "abort";

export class ApiError extends Error {
  status: number;
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null;
  errorType: ApiErrorType;

  constructor(
    status: number,
    message: string,
    errorType: ApiErrorType,
    detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null = null
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.errorType = errorType;
    this.detail = detail;
  }
}

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";
const DEFAULT_TIMEOUT_MS = 15000;

let refreshPromise: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  if (refreshPromise) {
    return refreshPromise;
  }

  refreshPromise = (async () => {
    const response = await fetch(`${BASE_URL}/auth/refresh`, {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new ApiError(response.status, "Session expired. Please log in again.", "http");
    }

    const data = (await response.json()) as { data?: { accessToken?: string } };
    const accessToken = data?.data?.accessToken;

    if (!accessToken) {
      throw new ApiError(500, "Session refresh failed. Please log in again.", "parse");
    }

    return accessToken;
  })();

  try {
    return await refreshPromise;
  } finally {
    refreshPromise = null;
  }
}

interface RequestOptions extends RequestInit {
  timeoutMs?: number;
  signal?: AbortSignal;
  skipAuthRetry?: boolean;
}

async function parseResponseBody(response: Response): Promise<unknown> {
  const contentType = response.headers.get("Content-Type");
  const isJson = contentType !== null && contentType.includes("application/json");
  const rawText = await response.text();

  if (rawText.length === 0) {
    return null;
  }

  if (isJson) {
    try {
      return JSON.parse(rawText);
    } catch {
      throw new ApiError(
        response.status,
        "The server returned a malformed response. Please try again.",
        "parse"
      );
    }
  }

  return rawText;
}

async function request<T>(endpoint: string, options: RequestOptions = {}): Promise<T> {
  const {
    timeoutMs = DEFAULT_TIMEOUT_MS,
    signal: externalSignal,
    skipAuthRetry,
    ...init
  } = options;

  const url = `${BASE_URL}${endpoint}`;

  const headers = new Headers(init.headers);
  if (!(init.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const timeoutController = new AbortController();
  const timeoutId = setTimeout(() => timeoutController.abort(), timeoutMs);

  const onExternalAbort = () => timeoutController.abort();
  if (externalSignal) {
    if (externalSignal.aborted) {
      timeoutController.abort();
    } else {
      externalSignal.addEventListener("abort", onExternalAbort);
    }
  }

  const config: RequestInit = {
    ...init,
    headers,
    credentials: "include",
    signal: timeoutController.signal,
  };

  try {
    let response: Response;
    try {
      response = await fetch(url, config);
    } catch (fetchError) {
      if (fetchError instanceof DOMException && fetchError.name === "AbortError") {
        if (externalSignal?.aborted) {
          throw new ApiError(0, "Request was cancelled.", "abort");
        }
        throw new ApiError(0, "The request timed out. Please try again.", "network");
      }
      throw new ApiError(0, "Unable to reach the server. Check your connection.", "network");
    }

    if (response.status === 204) {
      return {} as T;
    }

    if (response.status === 401 && !skipAuthRetry && endpoint !== "/auth/refresh") {
      try {
        await refreshAccessToken();
      } catch {
        throw new ApiError(401, "Your session has expired. Please log in again.", "http");
      }
      return request<T>(endpoint, { ...options, skipAuthRetry: true });
    }

    const responseData = await parseResponseBody(response);

    if (!response.ok) {
      const errorData = responseData as ApiErrorResponse | null;
      let errorMessage = "An unexpected error occurred. Please try again.";

      if (errorData && typeof errorData.detail === "string") {
        errorMessage = errorData.detail;
      } else if (errorData && Array.isArray(errorData.detail)) {
        errorMessage = errorData.detail.map((err) => `${err.loc.join(".")}: ${err.msg}`).join(", ");
      } else if (errorData && errorData.message) {
        errorMessage = errorData.message;
      }

      throw new ApiError(response.status, errorMessage, "http", errorData?.detail ?? null);
    }

    return responseData as T;
  } finally {
    clearTimeout(timeoutId);
    if (externalSignal) {
      externalSignal.removeEventListener("abort", onExternalAbort);
    }
  }
}

export const apiClient = {
  get: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "GET" }),
  post: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "POST",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  put: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PATCH",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  delete: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "DELETE" }),
};
