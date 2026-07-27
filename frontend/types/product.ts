// Mirrors: app/schemas/product.py, app/schemas/product_variant.py, app/schemas/category.py, app/schemas/product_category.py

export interface Category {
  id: number;
  name: string;
  description: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface CategoryCreate {
  name: string;
  description?: string | null;
}

export interface CategoryUpdate {
  name?: string;
  description?: string | null;
}

export interface Product {
  id: number;
  name: string;
  description: string | null;
  price: number;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
  categories: Category[];
}

export interface ProductCreate {
  name: string;
  description?: string | null;
  price: number;
  isActive?: boolean;
}

export interface ProductUpdate {
  name?: string;
  description?: string | null;
  price?: number;
  isActive?: boolean;
}

export interface ProductVariant {
  id: number;
  productId: number;
  sku: string;
  price: number;
  stockQuantity: number;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface ProductVariantCreate {
  sku: string;
  price: number;
  stockQuantity?: number;
  isActive?: boolean;
}

export interface ProductVariantUpdate {
  sku?: string;
  price?: number;
  stockQuantity?: number;
  isActive?: boolean;
}

export interface ProductCategory {
  id: number;
  productId: number;
  categoryId: number;
  category: Category;
  createdAt: string;
  updatedAt: string;
}

export interface ProductCategoryCreate {
  categoryId: number;
}
