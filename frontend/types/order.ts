// Mirrors: app/schemas/order.py, app/schemas/order_item.py, app/schemas/customer_order.py

export interface OrderItem {
  id: number;
  orderId: number;
  productVariantId: number | null;
  quantity: number;
  priceAtPurchase: number;
  createdAt: string;
  updatedAt: string;
}

export interface OrderItemCreate {
  productVariantId: number;
  quantity: number;
  priceAtPurchase: number;
}

export interface OrderItemUpdate {
  quantity?: number;
  priceAtPurchase?: number;
}

export interface Order {
  id: number;
  customerId: number | null;
  status: string | null;
  guestName: string | null;
  guestEmail: string | null;
  guestPhone: string | null;
  shippingAddressId: number | null;
  billingAddressId: number | null;
  couponId: number | null;
  orderStatus: string;
  subtotal: number;
  discountAmount: number;
  shippingAmount: number;
  taxAmount: number;
  totalAmount: number;
  notes: string | null;
  createdAt: string;
  placedAt: string | null;
  items: OrderItem[];
}

export interface OrderCreate {
  customerId?: number | null;
  guestName?: string;
  guestEmail?: string;
  guestPhone?: string;
  orderStatus?: string;
}

export interface OrderUpdate {
  orderStatus?: string;
  notes?: string;
}

export interface OrderStatusUpdate {
  status: string;
}

export interface CustomerOrder {
  id: number;
  customerName: string | null;
  orderStatus: string;
  totalAmount: number;
  createdAt: string;
  items: OrderItem[];
}

export interface ReturnRequestCreate {
  orderItemId: number;
  reason?: string;
}

export interface ReturnRequestStatusUpdate {
  status: string;
  refundAmount?: number;
}

export interface ReturnRequest {
  id: number;
  orderItemId: number;
  customerId: number;
  reason: string | null;
  status: string;
  refundAmount: number | null;
  requestedAt: string;
  processedAt: string | null;
}
