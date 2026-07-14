export interface ProductImage {
  id: string;
  url: string;
  altText?: string;
  isPrimary: boolean;
}

export interface ProductInventory {
  id: string;
  sku: string;
  quantity: number;
  lowStockThreshold: number;
}

export interface Product {
  id: string;
  slug: string;
  title: string;
  description: string;
  price: number;
  compareAtPrice?: number;
  category: string;
  images: ProductImage[];
  inventory: ProductInventory;
  ratingAverage: number;
  ratingCount: number;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}
