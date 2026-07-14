import { apiClient, ApiError } from "./client";
import { ApiResponse } from "@/types/api";
import { UserProfile, UserAddress } from "@/types/user";
import { AddressSchemaType } from "@/lib/validation/address";

const FALLBACK_MESSAGES = {
  getProfile: "We couldn't load your profile right now. Please try again.",
  updateProfile: "We couldn't save your profile changes. Please try again.",
  getAddresses: "We couldn't load your addresses right now. Please try again.",
  createAddress: "We couldn't save that address. Please try again.",
  updateAddress: "We couldn't update that address. Please try again.",
  deleteAddress: "We couldn't remove that address. Please try again.",
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

export async function getUserProfile(signal?: AbortSignal): Promise<ApiResponse<UserProfile>> {
  try {
    return await apiClient.get<ApiResponse<UserProfile>>("/users/profile", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProfile);
  }
}

export async function updateUserProfile(
  profileData: Partial<UserProfile>,
  signal?: AbortSignal
): Promise<ApiResponse<UserProfile>> {
  try {
    return await apiClient.patch<ApiResponse<UserProfile>>("/users/profile", profileData, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateProfile);
  }
}

export async function getUserAddresses(signal?: AbortSignal): Promise<ApiResponse<UserAddress[]>> {
  try {
    return await apiClient.get<ApiResponse<UserAddress[]>>("/users/addresses", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getAddresses);
  }
}

export async function createUserAddress(
  addressData: AddressSchemaType,
  signal?: AbortSignal
): Promise<ApiResponse<UserAddress>> {
  try {
    return await apiClient.post<ApiResponse<UserAddress>>("/users/addresses", addressData, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createAddress);
  }
}

export async function updateUserAddress(
  addressId: string,
  addressData: Partial<AddressSchemaType>,
  signal?: AbortSignal
): Promise<ApiResponse<UserAddress>> {
  try {
    return await apiClient.put<ApiResponse<UserAddress>>(
      `/users/addresses/${addressId}`,
      addressData,
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateAddress);
  }
}

export async function deleteUserAddress(
  addressId: string,
  signal?: AbortSignal
): Promise<ApiResponse<null>> {
  try {
    return await apiClient.delete<ApiResponse<null>>(`/users/addresses/${addressId}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.deleteAddress);
  }
}
