import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, OrderQueryParams } from "@/types/api";
import { Order } from "@/types/order";

const FALLBACK_MESSAGES = {
  getOrders: "We couldn't load your orders right now. Please try again.",
  getOrderById: "We couldn't load that order right now. Please try again.",
  createOrder: "We couldn't place your order. Please try again.",
  cancelOrder: "We couldn't cancel that order. Please try again.",
  requestOrderReturn: "We couldn't submit your return request. Please try again.",
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

export async function getOrders(
  params?: OrderQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Order>>> {
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
    return await apiClient.get<ApiResponse<PaginatedResponse<Order>>>(`/orders${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrders);
  }
}

export async function getOrderById(
  orderId: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.get<ApiResponse<Order>>(`/orders/${orderId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrderById);
  }
}

export async function createOrder(
  orderData: {
    addressId: string;
    paymentIntentId: string;
  },
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>("/orders", orderData, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createOrder);
  }
}

export async function cancelOrder(
  orderId: string,
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/cancel`,
      { reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.cancelOrder);
  }
}

export async function requestOrderReturn(
  orderId: string,
  itemIds: string[],
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/return`,
      { itemIds, reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.requestOrderReturn);
  }
}
