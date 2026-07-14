import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, ProductQueryParams } from "@/types/api";
import { Product } from "@/types/product";

const FALLBACK_MESSAGES = {
  getProducts: "We couldn't load products right now. Please try again.",
  getProductBySlug: "We couldn't load that product right now. Please try again.",
  getProductById: "We couldn't load that product right now. Please try again.",
  getCategories: "We couldn't load product categories right now. Please try again.",
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

export async function getProducts(
  params?: ProductQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Product>>> {
  try {
    const searchParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          searchParams.append(key, String(value));
        }
      });
    }
    const query = searchParams.toString() ? `?${searchParams.toString()}` : "";
    return await apiClient.get<ApiResponse<PaginatedResponse<Product>>>(`/products${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProducts);
  }
}

export async function getProductBySlug(
  slug: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/slug/${slug}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductBySlug);
  }
}

export async function getProductById(
  id: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/${id}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductById);
  }
}

export async function getCategories(signal?: AbortSignal): Promise<ApiResponse<string[]>> {
  try {
    return await apiClient.get<ApiResponse<string[]>>("/products/categories", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getCategories);
  }
}
