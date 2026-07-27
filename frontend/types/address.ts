// Mirrors: app/schemas/address.py

export interface Address {
  id: number;
  customerId: number;
  country: string;
  state: string | null;
  city: string;
  postalCode: string | null;
  addressLine1: string;
  addressLine2: string | null;
  isDefault: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface AddressCreate {
  country: string;
  state?: string | null;
  city: string;
  postalCode?: string | null;
  addressLine1: string;
  addressLine2?: string | null;
  isDefault?: boolean;
}

export interface AddressUpdate {
  country?: string;
  state?: string;
  city?: string;
  postalCode?: string;
  addressLine1?: string;
  addressLine2?: string;
  isDefault?: boolean;
}
