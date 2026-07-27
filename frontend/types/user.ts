// Mirrors: app/schemas/user.py, app/schemas/role.py, app/schemas/customer_profile.py

export interface Role {
  id: number;
  name: string;
  description: string | null;
}

export interface User {
  id: number;
  name: string;
  email: string;
  phoneNumber: string | null;
  avatarUrl: string | null;
  roleId: number;
  role: Role;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface UserCreate {
  name: string;
  email: string;
  password: string;
  phoneNumber?: string | null;
  avatarUrl?: string | null;
  roleId: number;
  isActive?: boolean;
}

export interface UserUpdate {
  name?: string;
  email?: string;
  phoneNumber?: string;
  avatarUrl?: string;
  roleId?: number;
  isActive?: boolean;
}

export interface CustomerProfile {
  id: number;
  name: string;
  email: string;
  phoneNumber: string | null;
  avatarUrl: string | null;
  emailVerified: boolean;
  createdAt: string;
}

export interface CustomerProfileUpdate {
  name?: string;
  phoneNumber?: string;
  avatarUrl?: string;
}
