export interface User {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  role: "user" | "admin" | "manager";
  isActive: boolean;
  createdAt: string;
}

export interface UserProfile {
  id: string;
  userId: string;
  phoneNumber?: string;
  avatarUrl?: string;
  dateOfBirth?: string;
  gender?: string;
}

export interface UserAddress {
  id: string;
  userId: string;
  title: string;
  streetAddress: string;
  apartment?: string;
  city: string;
  state: string;
  postalCode: string;
  country: string;
  isDefault: boolean;
}
