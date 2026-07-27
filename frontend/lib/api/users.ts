import { apiClient, ApiError } from "./client";
import { CustomerProfile, CustomerProfileUpdate } from "@/types/user";
import { Address, AddressCreate, AddressUpdate } from "@/types/address";

const BASE = "/customer/profile";

const FALLBACK_MESSAGES = {
  getProfile: "We couldn't load your profile. Please try again.",
  updateProfile: "We couldn't update your profile. Please try again.",
  listAddresses: "We couldn't load your addresses. Please try again.",
  createAddress: "We couldn't add that address. Please try again.",
  updateAddress: "We couldn't update that address. Please try again.",
  deleteAddress: "We couldn't delete that address. Please try again.",
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

// GET /customer/profile/me
export async function getProfile(signal?: AbortSignal): Promise<CustomerProfile> {
  try {
    return await apiClient.get<CustomerProfile>(`${BASE}/me`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProfile);
  }
}

// PUT /customer/profile/me
export async function updateProfile(
  data: CustomerProfileUpdate,
  signal?: AbortSignal
): Promise<CustomerProfile> {
  try {
    return await apiClient.put<CustomerProfile>(`${BASE}/me`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateProfile);
  }
}

// GET /customer/profile/addresses
export async function listAddresses(signal?: AbortSignal): Promise<Address[]> {
  try {
    return await apiClient.get<Address[]>(`${BASE}/addresses`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.listAddresses);
  }
}

// POST /customer/profile/addresses
export async function createAddress(data: AddressCreate, signal?: AbortSignal): Promise<Address> {
  try {
    return await apiClient.post<Address>(`${BASE}/addresses`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createAddress);
  }
}

// PUT /customer/profile/addresses/{addressId}
export async function updateAddress(
  addressId: number,
  data: AddressUpdate,
  signal?: AbortSignal
): Promise<Address> {
  try {
    return await apiClient.put<Address>(`${BASE}/addresses/${addressId}`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateAddress);
  }
}

// DELETE /customer/profile/addresses/{addressId} — 204 No Content
export async function deleteAddress(addressId: number, signal?: AbortSignal): Promise<void> {
  try {
    await apiClient.delete(`${BASE}/addresses/${addressId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.deleteAddress);
  }
}
