# Customer-domain re-export.
# orders/order_items/return_requests are single shared tables — the ORM
# models live in app/models/order.py, app/models/order_item.py, and
# app/models/return_request.py. This module re-exports them under the
# customer namespace so customer_order router/schema imports stay
# consistent, without creating a second mapper on the same tables.

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.return_request import ReturnRequest

__all__ = ["Order", "OrderItem", "ReturnRequest"]