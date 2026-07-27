export interface ApiErrorResponse {
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }>;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  size: number;
  pages: number;
}

// Mirrors: app/schemas/customer_auth.py CustomerToken
export interface AuthTokenResponse {
  accessToken: string;
  refreshToken: string;
  tokenType: string;
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
