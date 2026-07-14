import { User, UserProfile } from "./user";
import { Product } from "./product";
import { Order } from "./order";

export interface ApiResponse<T> {
  data: T;
  message?: string;
  status: number;
}

export interface ApiErrorResponse {
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }>;
  message?: string;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  size: number;
  pages: number;
}

export interface AuthResponseData {
  accessToken: string;
  refreshToken: string;
  user: User;
}

export interface ProductQueryParams {
  page?: number;
  size?: number;
  search?: string;
  category?: string;
  minPrice?: number;
  maxPrice?: number;
  sortBy?: string;
  sortOrder?: "asc" | "desc";
}

export interface OrderQueryParams {
  page?: number;
  size?: number;
  status?: string;
}

export interface CartItemResponse {
  id: string;
  productId: string;
  product: Product;
  quantity: number;
  priceAtAddition: number;
}

export interface CartResponseData {
  id: string;
  userId: string;
  items: CartItemResponse[];
  subtotal: number;
  tax: number;
  shipping: number;
  total: number;
}
