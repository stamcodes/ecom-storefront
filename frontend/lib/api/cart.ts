import { apiClient, ApiError } from "./client";
import { ApiResponse, CartResponseData } from "@/types/api";

const FALLBACK_MESSAGES = {
  get: "We couldn't load your cart right now. Please refresh and try again.",
  add: "We couldn't add that item to your cart. Please try again.",
  update: "We couldn't update that item's quantity. Please try again.",
  remove: "We couldn't remove that item from your cart. Please try again.",
  clear: "We couldn't clear your cart. Please try again.",
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

export async function getCart(signal?: AbortSignal): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.get<ApiResponse<CartResponseData>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.get);
  }
}

export async function addToCart(
  productId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.post<ApiResponse<CartResponseData>>(
      "/cart/items",
      { productId, quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.add);
  }
}

export async function updateCartItem(
  itemId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.put<ApiResponse<CartResponseData>>(
      `/cart/items/${itemId}`,
      { quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.update);
  }
}

export async function removeCartItem(
  itemId: string,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.delete<ApiResponse<CartResponseData>>(`/cart/items/${itemId}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.remove);
  }
}

export async function clearCart(signal?: AbortSignal): Promise<ApiResponse<null>> {
  try {
    return await apiClient.delete<ApiResponse<null>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.clear);
  }
}
