import { Product } from "./product";

export type OrderStatus =
  "pending" | "processing" | "shipped" | "delivered" | "cancelled" | "returned";

export interface OrderItem {
  id: string;
  orderId: string;
  productId: string;
  product: Product;
  quantity: number;
  priceAtPurchase: number;
}

export interface OrderShippingAddress {
  id: string;
  streetAddress: string;
  apartment?: string;
  city: string;
  state: string;
  postalCode: string;
  country: string;
}

export interface Order {
  id: string;
  userId: string;
  status: OrderStatus;
  items: OrderItem[];
  shippingAddress: OrderShippingAddress;
  subtotal: number;
  tax: number;
  shippingFee: number;
  total: number;
  paymentIntentId?: string;
  trackingNumber?: string;
  estimatedDelivery?: string;
  cancelledAt?: string;
  cancelReason?: string;
  createdAt: string;
  updatedAt: string;
}
