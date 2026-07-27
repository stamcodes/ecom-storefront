This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
backend/
  alembic/
    versions/
      3d77d5196130_add_phone_and_avatar_to_users.py
      d129ebf1174b_add_payments_table_model_sync.py
      ec78b9a97891_add_storefront_models_and_relations.py
    env.py
    README
    script.py.mako
  app/
    api/
      routes/
        auth.py
        cart.py
        categories.py
        checkout.py
        customer_auth.py
        customer_order.py
        customer_profiles.py
        order_items.py
        orders.py
        payments.py
        permissions.py
        product_categories.py
        product_variants.py
        products.py
        reviews.py
        role_permissions.py
        roles.py
        users.py
        wishlist.py
    core/
      auth.py
      cart_helpers.py
      config.py
      email.py
      jwt.py
      permissions.py
      security.py
      test_seed.py
    database/
      base.py
      session.py
    models/
      __init__.py
      address.py
      cart_item.py
      cart.py
      category.py
      coupon.py
      customer_order.py
      customer_profile.py
      order_item.py
      order.py
      payment.py
      permission.py
      product_category.py
      product_variant.py
      product.py
      return_request.py
      review.py
      role_permission.py
      role.py
      user.py
      wishlist.py
    repositories/
      cart_repository.py
    schemas/
      __init__.py
      address.py
      auth.py
      cart.py
      category.py
      customer_auth.py
      customer_order.py
      customer_profile.py
      order_item.py
      order.py
      permission.py
      product_category.py
      product_variant.py
      product.py
      review.py
      role_permission.py
      role.py
      user.py
      wishlist.py
    main.py
    seed.py
  tests/
    __init__.py
    conftest.py
    test_checkout.py
    test_customer_auth.py
    test_customer_order.py
    test_customer_profiles.py
    test_payments.py
    test_reviews.py
    test_wishlist.py
  .dockerignore
  alembic.ini
  Dockerfile
  pytest.ini
  requirements-dev.txt
  requirements.txt
frontend/
  .claude/
    rules/
      guardrails.md
  .github/
    copilot-instructions.md
  app/
    _(auth)/
      forgot-password/
        page.tsx
      login/
        page.tsx
      register/
        page.tsx
      reset-password/
        page.tsx
      verify-email/
        page.tsx
      layout.tsx
    _(protected)/
      account/
        page.tsx
      addresses/
        page.tsx
      chat-history/
        page.tsx
      checkout/
        order-confirmation/
          [orderId]/
            page.tsx
        page.tsx
      notifications/
        page.tsx
      orders/
        [orderId]/
          return/
            page.tsx
          page.tsx
        page.tsx
      profile/
        page.tsx
      settings/
        page.tsx
      wishlist/
        page.tsx
      layout.tsx
    _(public)/
      about/
        page.tsx
      cart/
        page.tsx
      categories/
        [slug]/
          page.tsx
        page.tsx
      contact/
        page.tsx
      faq/
        page.tsx
      privacy/
        page.tsx
      products/
        [slug]/
          loading.tsx
          page.tsx
        loading.tsx
        page.tsx
      return-policy/
        page.tsx
      search/
        page.tsx
      terms/
        page.tsx
      layout.tsx
      loading.tsx
      page.tsx
    api/
      auth/
        login/
          route.ts
        logout/
          route.ts
      checkout/
        create-payment-intent/
          route.ts
      webhooks/
        stripe/
          route.ts
    error.tsx
    globals.css
    layout.tsx
    not-found.tsx
    page.tsx
    robots.ts
    sitemap.ts
  e2e/
    auth.spec.ts
    checkout.spec.ts
    phase1-checkpoint.spec.ts
  hooks/
    useDebouncedValue.ts
    useOrderStatusPolling.ts
    useWebSocket.ts
  lib/
    api/
      auth.ts
      cart.ts
      client.ts
      notifications.ts
      orders.ts
      products.ts
      reviews.ts
      users.ts
      wishlist.ts
    stores/
      authStore.ts
      cartStore.ts
      checkoutStore.ts
      notificationStore.ts
      wishlistStore.ts
    stripe/
      client.ts
      paymentIntent.ts
    utils/
      format.ts
    validation/
      address.ts
      auth.ts
      contact.ts
      review.ts
    websocket/
      chatConnection.ts
      connectionManager.ts
  tests/
    smoke.test.tsx
  types/
    address.ts
    api.ts
    auth.ts
    cart.ts
    category.ts
    chats.ts
    notification.ts
    order.ts
    product.ts
    review.ts
    role.ts
    user.ts
    wishlist.ts
  .env.example
  .prettierrc
  eslint.config.mjs
  gitignore
  jest.config.ts
  jest.setup.ts
  next.config.ts
  package.json
  playwright.config.ts
  postcss.config.js
  PROGRESS.md
  tsconfig.jest.json
  tsconfig.json
  update_progress.py
.gitignore
package.json
```

# Files

## File: backend/alembic/versions/3d77d5196130_add_phone_and_avatar_to_users.py
````python
"""add_phone_and_avatar_to_users

Revision ID: 3d77d5196130
Revises: ec78b9a97891
Create Date: 2026-07-14 17:02:56.416928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d77d5196130'
down_revision: Union[str, Sequence[str], None] = 'ec78b9a97891'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(length=20), nullable=True))
    op.add_column('users', sa.Column('avatar_url', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_url')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
````

## File: backend/alembic/versions/d129ebf1174b_add_payments_table_model_sync.py
````python
"""add payments table model sync

Revision ID: d129ebf1174b
Revises: 3d77d5196130
Create Date: 2026-07-23 19:06:17.245688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd129ebf1174b'
down_revision: Union[str, Sequence[str], None] = '3d77d5196130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupon_redemptions')
    op.drop_table('variant_values')
    op.drop_table('product_variant_options')
    op.drop_table('coupon_categories')
    op.drop_table('review_images')
    op.drop_table('order_status_history')
    op.drop_table('chat_messages')
    op.drop_table('chat_threads')
    op.drop_table('notifications')
    op.drop_table('product_promotions')
    op.drop_table('product_variant_images')
    op.drop_table('return_requests')
    op.drop_table('variant_types')
    op.drop_table('wishlist_items')
    op.drop_table('promotions')
    op.alter_column('addresses', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=False)
    op.drop_constraint(op.f('uq_cart_variant'), 'cart_items', type_='unique')
    op.create_index(op.f('ix_cart_items_id'), 'cart_items', ['id'], unique=False)
    op.drop_constraint(op.f('fk_cart_items_product_variant'), 'cart_items', type_='foreignkey')
    op.create_foreign_key(None, 'cart_items', 'product_variants', ['product_variant_id'], ['id'])
    op.drop_constraint(op.f('carts_guest_token_key'), 'carts', type_='unique')
    op.create_index(op.f('ix_carts_guest_token'), 'carts', ['guest_token'], unique=True)
    op.create_index(op.f('ix_carts_id'), 'carts', ['id'], unique=False)
    op.drop_constraint(op.f('coupons_code_key'), 'coupons', type_='unique')
    op.create_index(op.f('ix_coupons_code'), 'coupons', ['code'], unique=True)
    op.create_index(op.f('ix_coupons_id'), 'coupons', ['id'], unique=False)
    op.create_index(op.f('ix_customer_profiles_id'), 'customer_profiles', ['id'], unique=False)
    op.drop_column('order_items', 'tax_amount')
    op.drop_column('order_items', 'discount_amount')
    op.add_column('orders', sa.Column('created_by_user_id', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('status', sa.String(length=20), nullable=False))
    op.add_column('orders', sa.Column('customer_name', sa.String(length=100), nullable=True))
    op.alter_column('orders', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(op.f('fk_orders_coupon'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_billing_address'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_shipping_address'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_customer'), 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'customer_profiles', ['customer_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'orders', 'users', ['created_by_user_id'], ['id'], ondelete='SET NULL')
    op.drop_column('orders', 'coupon_id')
    op.drop_column('orders', 'notes')
    op.drop_column('orders', 'placed_at')
    op.drop_column('orders', 'tax_amount')
    op.drop_column('orders', 'shipping_amount')
    op.drop_column('orders', 'order_status')
    op.drop_column('orders', 'discount_amount')
    op.drop_column('orders', 'billing_address_id')
    op.drop_column('orders', 'subtotal')
    op.drop_column('orders', 'guest_phone')
    op.drop_column('orders', 'guest_email')
    op.drop_column('orders', 'shipping_address_id')
    op.drop_column('orders', 'guest_name')
    op.add_column('payments', sa.Column('provider', sa.String(length=50), nullable=True))
    op.add_column('payments', sa.Column('stripe_payment_intent_id', sa.String(length=255), nullable=True))
    op.add_column('payments', sa.Column('status', sa.String(length=20), nullable=False))
    op.alter_column('payments', 'payment_method',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint(op.f('payments_order_id_key'), 'payments', type_='unique')
    op.drop_constraint(op.f('payments_transaction_reference_key'), 'payments', type_='unique')
    op.create_index(op.f('ix_payments_id'), 'payments', ['id'], unique=False)
    op.create_index(op.f('ix_payments_stripe_payment_intent_id'), 'payments', ['stripe_payment_intent_id'], unique=True)
    op.drop_column('payments', 'paid_at')
    op.drop_column('payments', 'payment_status')
    op.drop_column('payments', 'transaction_reference')
    op.drop_column('payments', 'payment_provider')
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.add_column('payments', sa.Column('payment_provider', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('payments', sa.Column('transaction_reference', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('payments', sa.Column('payment_status', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.add_column('payments', sa.Column('paid_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_payments_stripe_payment_intent_id'), table_name='payments')
    op.drop_index(op.f('ix_payments_id'), table_name='payments')
    op.create_unique_constraint(op.f('payments_transaction_reference_key'), 'payments', ['transaction_reference'], postgresql_nulls_not_distinct=False)
    op.create_unique_constraint(op.f('payments_order_id_key'), 'payments', ['order_id'], postgresql_nulls_not_distinct=False)
    op.alter_column('payments', 'payment_method',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_column('payments', 'status')
    op.drop_column('payments', 'stripe_payment_intent_id')
    op.drop_column('payments', 'provider')
    op.add_column('orders', sa.Column('guest_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('shipping_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('guest_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('guest_phone', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('subtotal', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('billing_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('discount_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('order_status', sa.VARCHAR(length=20), server_default=sa.text("'open'::character varying"), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('shipping_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('tax_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('placed_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(op.f('fk_orders_customer'), 'orders', 'customer_profiles', ['customer_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_shipping_address'), 'orders', 'addresses', ['shipping_address_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_billing_address'), 'orders', 'addresses', ['billing_address_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_coupon'), 'orders', 'coupons', ['coupon_id'], ['id'], ondelete='SET NULL')
    op.alter_column('orders', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('orders', 'customer_name')
    op.drop_column('orders', 'status')
    op.drop_column('orders', 'created_by_user_id')
    op.add_column('order_items', sa.Column('discount_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('order_items', sa.Column('tax_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_customer_profiles_id'), table_name='customer_profiles')
    op.drop_index(op.f('ix_coupons_id'), table_name='coupons')
    op.drop_index(op.f('ix_coupons_code'), table_name='coupons')
    op.create_unique_constraint(op.f('coupons_code_key'), 'coupons', ['code'], postgresql_nulls_not_distinct=False)
    op.drop_index(op.f('ix_carts_id'), table_name='carts')
    op.drop_index(op.f('ix_carts_guest_token'), table_name='carts')
    op.create_unique_constraint(op.f('carts_guest_token_key'), 'carts', ['guest_token'], postgresql_nulls_not_distinct=False)
    op.drop_constraint(None, 'cart_items', type_='foreignkey')
    op.create_foreign_key(op.f('fk_cart_items_product_variant'), 'cart_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_cart_items_id'), table_name='cart_items')
    op.create_unique_constraint(op.f('uq_cart_variant'), 'cart_items', ['cart_id', 'product_variant_id'], postgresql_nulls_not_distinct=False)
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.alter_column('addresses', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('promotions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('discount_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('discount_value', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('start_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('end_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("discount_type::text = ANY (ARRAY['percentage'::character varying, 'fixed'::character varying]::text[])", name=op.f('promotions_discount_type_check')),
    sa.CheckConstraint('discount_value >= 0::numeric', name=op.f('promotions_discount_value_check')),
    sa.CheckConstraint('end_date > start_date', name=op.f('chk_promotion_dates')),
    sa.PrimaryKeyConstraint('id', name=op.f('promotions_pkey'))
    )
    op.create_table('wishlist_items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_wishlist_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_wishlist_product'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('wishlist_items_pkey')),
    sa.UniqueConstraint('customer_id', 'product_id', name=op.f('uq_customer_product_wishlist'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('variant_types',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_types_pkey'))
    )
    op.create_table('return_requests',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_item_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reason', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), server_default=sa.text("'pending'::character varying"), autoincrement=False, nullable=False),
    sa.Column('refund_amount', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.Column('admin_notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('requested_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('processed_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.CheckConstraint("status::text = ANY (ARRAY['pending'::character varying, 'approved'::character varying, 'rejected'::character varying, 'received'::character varying, 'refunded'::character varying, 'completed'::character varying]::text[])", name=op.f('return_requests_status_check')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_return_requests_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_item_id'], ['order_items.id'], name=op.f('fk_return_requests_order_item'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('return_requests_pkey'))
    )
    op.create_table('product_variant_images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=512), autoincrement=False, nullable=False),
    sa.Column('alt_text', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('display_order', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('is_primary', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('fk_product_variant_images_variant'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('product_variant_images_pkey'))
    )
    op.create_table('product_promotions',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('promotion_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_product_promotions_product'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotions.id'], name=op.f('fk_product_promotions_promotion'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product_id', 'promotion_id', name=op.f('product_promotions_pkey'))
    )
    op.create_table('notifications',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('notification_type', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('is_read', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('read_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.CheckConstraint("notification_type::text = ANY (ARRAY['order'::character varying, 'payment'::character varying, 'promotion'::character varying, 'coupon'::character varying, 'system'::character varying, 'account'::character varying]::text[])", name=op.f('notifications_notification_type_check')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_notifications_customer'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('notifications_pkey'))
    )
    op.create_table('chat_threads',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('guest_token', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), server_default=sa.text("'open'::character varying"), autoincrement=False, nullable=False),
    sa.Column('assigned_agent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("status::text = ANY (ARRAY['open'::character varying, 'assigned'::character varying, 'closed'::character varying]::text[])", name=op.f('chat_threads_status_check')),
    sa.ForeignKeyConstraint(['assigned_agent_id'], ['users.id'], name=op.f('fk_chat_threads_agent'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_chat_threads_customer'), ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name=op.f('chat_threads_pkey'))
    )
    op.create_table('chat_messages',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('thread_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sender_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('attachment_url', sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column('is_read', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("sender_type::text = ANY (ARRAY['customer'::character varying, 'guest'::character varying, 'agent'::character varying, 'system'::character varying]::text[])", name=op.f('chat_messages_sender_type_check')),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], name=op.f('fk_chat_messages_sender'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['thread_id'], ['chat_threads.id'], name=op.f('fk_chat_messages_thread'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('chat_messages_pkey'))
    )
    op.create_table('order_status_history',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('changed_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('changed_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['changed_by_user_id'], ['users.id'], name=op.f('fk_order_status_history_user'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_status_history_order'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('order_status_history_pkey'))
    )
    op.create_table('review_images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('review_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=512), autoincrement=False, nullable=False),
    sa.Column('alt_text', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('display_order', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], name=op.f('fk_review_images_review'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('review_images_pkey'))
    )
    op.create_table('coupon_categories',
    sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_coupon_categories_category'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupons.id'], name=op.f('fk_coupon_categories_coupon'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('coupon_id', 'category_id', name=op.f('coupon_categories_pkey'))
    )
    op.create_table('product_variant_options',
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('variant_value_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('product_variant_options_product_variant_id_fkey'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['variant_value_id'], ['variant_values.id'], name=op.f('product_variant_options_variant_value_id_fkey'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product_variant_id', 'variant_value_id', name=op.f('product_variant_options_pkey'))
    )
    op.create_table('variant_values',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('variant_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('value_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['variant_type_id'], ['variant_types.id'], name=op.f('fk_variant_values_variant_type'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_values_pkey'))
    )
    op.create_table('coupon_redemptions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('redeemed_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupons.id'], name=op.f('fk_coupon_redemptions_coupon'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_coupon_redemptions_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_coupon_redemptions_order'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('coupon_redemptions_pkey')),
    sa.UniqueConstraint('coupon_id', 'customer_id', 'order_id', name=op.f('uq_coupon_redemption'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    # ### end Alembic commands ###
````

## File: backend/alembic/versions/ec78b9a97891_add_storefront_models_and_relations.py
````python
"""add_storefront_models_and_relations

Revision ID: ec78b9a97891
Revises: 
Create Date: 2026-07-14 16:40:57.480891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ec78b9a97891'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    
    # 1. Drop tables in strict dependency order to prevent FK errors
    op.drop_table('product_variant_options')
    op.drop_table('variant_values')
    op.drop_table('variant_types')
    op.drop_table('knex_migrations_lock')
    op.drop_table('knex_migrations')
    
    # 2. Apply index additions and structural adjustments
    op.create_index(op.f('ix_branches_id'), 'branches', ['id'], unique=False)
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.alter_column('order_items', 'product_variant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_order_items_id'), 'order_items', ['id'], unique=False)
    op.drop_constraint(op.f('order_items_product_variant_id_foreign'), 'order_items', type_='foreignkey')
    op.create_foreign_key(None, 'order_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='SET NULL')
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=False)
    op.create_index(op.f('ix_product_categories_id'), 'product_categories', ['id'], unique=False)
    op.create_index(op.f('ix_product_variants_id'), 'product_variants', ['id'], unique=False)
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_index(op.f('ix_role_permissions_id'), 'role_permissions', ['id'], unique=False)
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_user_branches_id'), 'user_branches', ['id'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_constraint(op.f('users_role_id_foreign'), 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key(op.f('users_role_id_foreign'), 'users', 'roles', ['role_id'], ['id'], ondelete='RESTRICT')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_user_branches_id'), table_name='user_branches')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_index(op.f('ix_role_permissions_id'), table_name='role_permissions')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_index(op.f('ix_product_variants_id'), table_name='product_variants')
    op.drop_index(op.f('ix_product_categories_id'), table_name='product_categories')
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint(None, 'order_items', type_='foreignkey')
    op.create_foreign_key(op.f('order_items_product_variant_id_foreign'), 'order_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='RESTRICT')
    op.drop_index(op.f('ix_order_items_id'), table_name='order_items')
    op.alter_column('order_items', 'product_variant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_index(op.f('ix_branches_id'), table_name='branches')
    op.create_table('product_variant_options',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('variant_value_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('product_variant_options_product_variant_id_foreign'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['variant_value_id'], ['variant_values.id'], name=op.f('product_variant_options_variant_value_id_foreign'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('product_variant_options_pkey')),
    sa.UniqueConstraint('product_variant_id', 'variant_value_id', name=op.f('product_variant_options_product_variant_id_variant_value_id_uni'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('variant_values',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('variant_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('value_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['variant_type_id'], ['variant_types.id'], name=op.f('variant_values_variant_type_id_foreign'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_values_pkey'))
    )
    op.create_table('knex_migrations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('batch', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('migration_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('knex_migrations_pkey'))
    )
    op.create_table('variant_types',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_types_pkey')),
    sa.UniqueConstraint('type_name', name=op.f('variant_types_type_name_unique'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('knex_migrations_lock',
    sa.Column('index', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('is_locked', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('index', name=op.f('knex_migrations_lock_pkey'))
    )
    # ### end Alembic commands ###
````

## File: backend/alembic/README
````
Generic single-database configuration.
````

## File: backend/alembic/script.py.mako
````
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}
````

## File: backend/app/api/routes/reviews.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.review import Review
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewOut, ReviewUpdate
from app.core.auth import get_current_user

router = APIRouter()


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("/products/{product_id}/reviews", response_model=list[ReviewOut])
async def get_product_reviews(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Review).where(Review.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/reviews", response_model=ReviewOut, status_code=201)
async def create_product_review(
    product_id: int,
    payload: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    profile = await _get_or_create_customer_profile(db, current_user)

    # TODO: BYPASSED VERIFIED-PURCHASE CHECK.
    # Checkout isn't built yet, so there's no real link from order_item_id -> this
    # customer. Once POST /checkout exists and Order has a customer_id, replace this
    # block with a real check, e.g.:
    #   - fetch OrderItem by payload.order_item_id
    #   - join to Order, confirm Order.customer_id == profile.id
    #   - confirm OrderItem.product_variant -> product_id == product_id
    #   - 404/403 if any of that fails
    # For now we only confirm the order_item_id points to a row that exists.
    from app.models.order_item import OrderItem
    result = await db.execute(select(OrderItem).where(OrderItem.id == payload.order_item_id))
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    new_review = Review(
        customer_id=profile.id,
        product_id=product_id,
        order_item_id=payload.order_item_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)
    return new_review


@router.put("/reviews/{review_id}", response_model=ReviewOut)
async def update_review(
    review_id: int,
    payload: ReviewUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only edit your own reviews")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(review, field, value)

    await db.commit()
    await db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=204)
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")

    await db.delete(review)
    await db.commit()
    return None
````

## File: backend/app/api/routes/wishlist.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.wishlist import Wishlist
from app.schemas.wishlist import WishlistCreate, WishlistResponse

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("", response_model=list[WishlistResponse])
async def get_wishlist(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(select(Wishlist).where(Wishlist.customer_id == profile.id))
    return result.scalars().all()


@router.post("", response_model=WishlistResponse, status_code=status.HTTP_201_CREATED)
async def add_to_wishlist(
    payload: WishlistCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    product = await db.execute(select(Product).where(Product.id == payload.product_id))
    if not product.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Product not found")

    existing = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == payload.product_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Product already in wishlist")

    item = Wishlist(customer_id=profile.id, product_id=payload.product_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_wishlist(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == product_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Product not found in wishlist")

    await db.delete(item)
    await db.commit()
````

## File: backend/app/core/cart_helpers.py
````python

````

## File: backend/app/core/email.py
````python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings

FROM_EMAIL = settings.FROM_EMAIL


def send_email(to: str, subject: str, body: str, html: bool = False) -> None:
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, [to], msg.as_string())


def send_verification_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    subject = "Verify your email"
    body = f"Click the link to verify your email: {link}\nThis link expires in 24 hours."
    send_email(to, subject, body)


def send_password_reset_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    subject = "Reset your password"
    body = f"Click the link to reset your password: {link}\nThis link expires in 1 hour."
    send_email(to, subject, body)
````

## File: backend/app/core/permissions.py
````python
from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.core.auth import get_current_user

ADMIN = 1
MANAGER = 2
STAFF = 3


def require_role(*allowed_role_ids: int):
    """
    Returns a FastAPI dependency that checks whether the current user's
    role_id is in the allowed list.

    Usage:
        @router.post("/products")
        def create_product(
            current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
        ):
            ...
    """

    def dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role_id not in allowed_role_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return dependency


def block_manager_on_admin_target(current_user: User, target_role_id: int):
    """
    Managers can manage roles/permissions for everyone except Admins.
    Call this after fetching the target resource's role_id.
    """
    if current_user.role_id == MANAGER and target_role_id == ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Managers cannot modify Admin-level roles or users",
        )
````

## File: backend/app/core/security.py
````python
import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)
````

## File: backend/app/core/test_seed.py
````python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from datetime import datetime, timedelta, timezone

BOGUS_PRODUCT_ID = 999001
BOGUS_VARIANT_ID = 999001
BOGUS_VARIANT_SKU = "BOGUS-TEST-SKU"
BOGUS_COUPON_CODE = "TESTCODE10"


async def ensure_bogus_data(db: AsyncSession) -> None:
    result = await db.execute(select(Product).where(Product.id == BOGUS_PRODUCT_ID))
    product = result.scalar_one_or_none()
    if not product:
        product = Product(
            id=BOGUS_PRODUCT_ID,
            name="Bogus Test Product",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            price=9.99,
            is_active=True,
        )
        db.add(product)
        await db.flush()

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == BOGUS_VARIANT_ID))
    variant = result.scalar_one_or_none()
    if not variant:
        variant = ProductVariant(
            id=BOGUS_VARIANT_ID,
            product_id=BOGUS_PRODUCT_ID,
            sku=BOGUS_VARIANT_SKU,
            price=9.99,
            stock_quantity=1000,
            is_active=True,
        )
        db.add(variant)

    result = await db.execute(select(Coupon).where(Coupon.code == BOGUS_COUPON_CODE))
    coupon = result.scalar_one_or_none()
    if not coupon:
        coupon = Coupon(
            code=BOGUS_COUPON_CODE,
            name="Bogus Test Coupon",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            discount_type="percentage",
            discount_value=10,
            minimum_order_amount=0,
            usage_limit=None,
            usage_count=0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=365),
            is_active=True,
        )
        db.add(coupon)

    await db.commit()
````

## File: backend/app/models/address.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship(back_populates="addresses")
````

## File: backend/app/models/coupon.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Coupon(Base):
    __tablename__ = "coupons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    discount_type: Mapped[str] = mapped_column(String(20), nullable=False)
    discount_value: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    minimum_order_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, default=0)
    usage_limit: Mapped[int | None] = mapped_column(Integer, nullable=True)
    usage_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    carts: Mapped[list["Cart"]] = relationship(back_populates="coupon")
````

## File: backend/app/models/customer_order.py
````python
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
````

## File: backend/app/models/customer_profile.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

   # Relationships
    user: Mapped["User"] = relationship(back_populates="customer_profile")
    cart: Mapped["Cart"] = relationship(back_populates="customer", uselist=False)
    addresses: Mapped[list["Address"]] = relationship(back_populates="customer")
````

## File: backend/app/models/payment.py
````python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)

    payment_method: Mapped[str | None] = mapped_column(String(50), nullable=True)
    provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    stripe_payment_intent_id: Mapped[str | None] = mapped_column(
        String(255), unique=True, nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False, default="usd")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    order: Mapped["Order"] = relationship()
````

## File: backend/app/models/permission.py
````python
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/product_category.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"
    __table_args__ = (
        UniqueConstraint("product_id", "category_id", name="product_categories_product_id_category_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="category_links")
    category: Mapped["Category"] = relationship(back_populates="product_links")
````

## File: backend/app/models/product_variant.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    sku: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="variants")
````

## File: backend/app/models/product.py
````python
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    category_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    variants: Mapped[list["ProductVariant"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    @property
    def categories(self) -> list["Category"]:
        return [link.category for link in self.category_links]
````

## File: backend/app/models/return_request.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ReturnRequest(Base):
    __tablename__ = "return_requests"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )

    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    refund_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)

    requested_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    processed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    order_item: Mapped["OrderItem"] = relationship()
    customer: Mapped["CustomerProfile"] = relationship()
````

## File: backend/app/models/review.py
````python
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="reviews_rating_check"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )

    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()
    order_item: Mapped["OrderItem"] = relationship()
````

## File: backend/app/models/role_permission.py
````python
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = (
        UniqueConstraint("role_id", "permission_id", name="role_permissions_role_id_permission_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role: Mapped["Role"] = relationship(back_populates="permission_links")
    permission: Mapped["Permission"] = relationship(back_populates="role_links")
````

## File: backend/app/models/role.py
````python
from sqlalchemy import (
    DateTime,
    Integer,
    String,
    func
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Role(Base):
    __tablename__ = "roles"

    # Primary Key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # Basic Fields
    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # Timestamps
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

     # Relationships
    users = relationship("User", back_populates="role")
    permission_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/wishlist.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Wishlist(Base):
    __tablename__ = "wishlist_items"
    __table_args__ = (
    UniqueConstraint("customer_id", "product_id", name="uq_customer_product_wishlist"),
)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()
````

## File: backend/app/repositories/cart_repository.py
````python

````

## File: backend/app/schemas/__init__.py
````python

````

## File: backend/app/schemas/address.py
````python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddressBase(BaseModel):
    country: str
    state: Optional[str] = None
    city: str
    postal_code: Optional[str] = None
    address_line_1: str
    address_line_2: Optional[str] = None
    is_default: bool = False


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    is_default: Optional[bool] = None


class AddressOut(AddressBase):
    id: int
    customer_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
````

## File: backend/app/schemas/customer_profile.py
````python
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class CustomerRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None


class EmailVerifyRequest(BaseModel):
    token: str


class CustomerProfileOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: Optional[str]
    avatar_url: Optional[str]
    email_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CustomerProfileUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
````

## File: backend/app/schemas/order_item.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class OrderItemOut(BaseModel):
    id: int
    order_id: int
    product_variant_id: int | None
    quantity: int
    price_at_purchase: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(gt=0)
    price_at_purchase: float = Field(gt=0)


class OrderItemUpdate(BaseModel):
    quantity: int | None = Field(default=None, gt=0)
    price_at_purchase: float | None = Field(default=None, gt=0)
````

## File: backend/app/schemas/permission.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class PermissionOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PermissionCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class PermissionUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
````

## File: backend/app/schemas/product_category.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.category import CategoryOut


class ProductCategoryOut(BaseModel):
    id: int
    product_id: int
    category_id: int
    category: CategoryOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductCategoryCreate(BaseModel):
    category_id: int
````

## File: backend/app/schemas/product_variant.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ProductVariantOut(BaseModel):
    id: int
    product_id: int
    sku: str
    price: float
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductVariantCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    is_active: bool = True


class ProductVariantUpdate(BaseModel):
    sku: str | None = Field(default=None, min_length=1, max_length=100)
    price: float | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    is_active: bool | None = None
````

## File: backend/app/schemas/product.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.category import CategoryOut


class ProductOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    is_active: bool
    created_at: datetime
    updated_at: datetime
    categories: list[CategoryOut] = []

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(gt=0)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    is_active: bool | None = None
````

## File: backend/app/schemas/review.py
````python
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReviewCreate(BaseModel):
    order_item_id: int
    rating: int = Field(ge=1, le=5)
    comment: str | None = None


class ReviewUpdate(BaseModel):
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = None


class ReviewOut(BaseModel):
    id: int
    customer_id: int
    product_id: int
    order_item_id: int
    rating: int
    comment: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
````

## File: backend/app/schemas/role_permission.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.permission import PermissionOut


class RolePermissionOut(BaseModel):
    id: int
    role_id: int
    permission_id: int
    permission: PermissionOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RolePermissionCreate(BaseModel):
    permission_id: int
````

## File: backend/app/schemas/role.py
````python
from pydantic import BaseModel, ConfigDict, Field


class RoleOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str | None = None


class RoleUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
````

## File: backend/app/schemas/wishlist.py
````python
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WishlistCreate(BaseModel):
    product_id: int


class WishlistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    product_id: int
    created_at: datetime
````

## File: backend/tests/__init__.py
````python

````

## File: backend/tests/test_checkout.py
````python
import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile
from app.models.product_variant import ProductVariant
from app.models.order import Order

pytestmark = pytest.mark.asyncio


async def test_checkout_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutsuccess@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=25.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=2)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["status"] == "open"
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 1
    assert body["items"][0]["quantity"] == 2

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_checkout_empty_cart(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutempty@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_no_cart_at_all(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutnocart@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]

    await db.refresh(variant)
    assert variant.stock_quantity == 1


async def test_checkout_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutinactive@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_checkout_clears_cart_items(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutclears@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=5)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201

    db.expire_all()

    second_resp = await client.post("/checkout", headers=headers)
    assert second_resp.status_code == 400
    assert second_resp.json()["detail"] == "Cart is empty"


async def test_checkout_unauthenticated(client):
    resp = await client.post("/checkout")
    assert resp.status_code == 401


async def test_checkout_multiple_items_total(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutmulti@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant_a = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant_a, quantity=3)

    from app.models.cart_item import CartItem
    variant_b = await make_product_variant(price=5.00, stock_quantity=10)
    db.add(CartItem(cart_id=cart.id, product_variant_id=variant_b.id, quantity=4))
    await db.commit()

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 2
````

## File: backend/tests/test_customer_auth.py
````python
import pytest
from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from app.models.user import User

pytestmark = pytest.mark.asyncio


async def test_register_success(client, mock_emails):
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "StrongPass123!",
        "phone_number": "+1234567890",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "jane@example.com"
    assert body["email_verified"] is False
    assert len(mock_emails["verification"]) == 1
    assert mock_emails["verification"][0][0] == "jane@example.com"


async def test_register_duplicate_email(client, make_customer):
    user, _ = await make_customer(email="dupe@example.com")
    payload = {
        "name": "Dupe",
        "email": "dupe@example.com",
        "password": "StrongPass123!",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Email already registered"


async def test_register_invalid_password_too_short(client):
    payload = {"name": "Jane", "email": "jane2@example.com", "password": "short"}
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 422


async def test_login_success(client, make_customer):
    user, password = await make_customer(email="login@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "login@example.com", "password": password})
    assert resp.status_code == 200
    body = resp.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


async def test_login_wrong_password(client, make_customer):
    await make_customer(email="wrongpass@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "wrongpass@example.com", "password": "WrongPass!"})
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid email or password"


async def test_login_nonexistent_email(client):
    resp = await client.post("/customer/auth/login", json={"email": "nouser@example.com", "password": "whatever123"})
    assert resp.status_code == 401


async def test_login_inactive_account(client, make_customer):
    await make_customer(email="inactive@example.com", active=False)
    resp = await client.post("/customer/auth/login", json={"email": "inactive@example.com", "password": "Password123!"})
    assert resp.status_code == 403
    assert resp.json()["detail"] == "Account is inactive"


async def test_verify_email_success(client, make_customer, db):
    user, _ = await make_customer(email="verify@example.com", verified=False)
    user.email_verification_token = "valid-token-123"
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "valid-token-123"})
    assert resp.status_code == 200

    result = await db.execute(select(User).where(User.email == "verify@example.com"))
    refreshed = result.scalar_one()
    assert refreshed.email_verified is True
    assert refreshed.email_verification_token is None


async def test_verify_email_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="expired@example.com", verified=False)
    user.email_verification_token = "expired-token"
    user.email_verification_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "expired-token"})
    assert resp.status_code == 400


async def test_verify_email_invalid_token(client):
    resp = await client.post("/customer/auth/verify-email", json={"token": "does-not-exist"})
    assert resp.status_code == 400


async def test_resend_verification_unverified_user(client, make_customer, mock_emails):
    await make_customer(email="resend@example.com", verified=False)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "resend@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 1


async def test_resend_verification_already_verified(client, make_customer, mock_emails):
    await make_customer(email="already@example.com", verified=True)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "already@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 0


async def test_resend_verification_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/resend-verification", json={"email": "ghost@example.com"})
    assert resp.status_code == 200
    assert "If that email exists" in resp.json()["message"]
    assert len(mock_emails["verification"]) == 0


async def test_forgot_password_existing_active_user(client, make_customer, mock_emails):
    await make_customer(email="forgot@example.com")
    resp = await client.post("/customer/auth/forgot-password", json={"email": "forgot@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 1


async def test_forgot_password_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/forgot-password", json={"email": "ghost2@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 0


async def test_reset_password_success(client, make_customer, db):
    user, _ = await make_customer(email="reset@example.com")
    user.password_reset_token = "reset-token-123"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "reset-token-123", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 200

    login_resp = await client.post(
        "/customer/auth/login", json={"email": "reset@example.com", "password": "NewStrongPass123!"}
    )
    assert login_resp.status_code == 200


async def test_reset_password_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="resetexp@example.com")
    user.password_reset_token = "expired-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "expired-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_invalid_token(client):
    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "not-a-real-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_inactive_account(client, make_customer, db):
    user, _ = await make_customer(email="resetinactive@example.com", active=False)
    user.password_reset_token = "inactive-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "inactive-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 403
````

## File: backend/tests/test_customer_order.py
````python
import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.customer_profile import CustomerProfile


async def _get_profile(db: AsyncSession, user) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    return result.scalar_one()


async def _make_order(
    db: AsyncSession,
    customer_id: int,
    order_status: str = "open",
    total_amount: float = 0,
) -> Order:
    order = Order(
        customer_id=customer_id,
        order_status=order_status,
        total_amount=total_amount,
    )
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order


async def _make_order_item(
    db: AsyncSession,
    order_id: int,
    variant,
    quantity: int = 2,
) -> OrderItem:
    item = OrderItem(
        order_id=order_id,
        product_variant_id=variant.id,
        quantity=quantity,
        price_at_purchase=variant.price,
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


# ---- Orders: cancel ----

@pytest.mark.asyncio
async def test_cancel_order_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["order_status"] == "cancelled"


@pytest.mark.asyncio
async def test_cancel_order_wrong_status(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_cancel_order_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner@example.com")
    other, _ = await make_customer(email="other@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: reorder ----

@pytest.mark.asyncio
async def test_reorder_creates_cart_items(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    await _make_order_item(db, order.id, variant, quantity=3)

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(user))

    assert response.status_code == 201
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_reorder_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner2@example.com")
    other, _ = await make_customer(email="other2@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: invoice ----

@pytest.mark.asyncio
async def test_get_invoice_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed", total_amount=100)

    response = await client.get(f"/orders/{order.id}/invoice", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_get_invoice_not_found(client: AsyncClient, make_customer, auth_headers):
    user, _ = await make_customer()

    response = await client.get("/orders/999999/invoice", headers=auth_headers(user))

    assert response.status_code == 404


# ---- Return Requests: create ----

@pytest.mark.asyncio
async def test_create_return_request_success(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )

    assert response.status_code == 201
    body = response.json()
    assert body["order_item_id"] == item.id
    assert body["status"] == "pending"


@pytest.mark.asyncio
async def test_create_return_request_duplicate(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )
    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size again"},
        headers=auth_headers(user),
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_return_request_item_not_owned(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    owner, _ = await make_customer(email="owner3@example.com")
    other, _ = await make_customer(email="other3@example.com")
    profile = await _get_profile(db, owner)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Not mine"},
        headers=auth_headers(other),
    )

    assert response.status_code == 404


# ---- Return Requests: list ----

@pytest.mark.asyncio
async def test_list_return_requests_scoped_to_customer(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user4@example.com")
    other, _ = await make_customer(email="other4@example.com")
    profile = await _get_profile(db, user)
    other_profile = await _get_profile(db, other)
    variant = await make_product_variant()

    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)
    other_order = await _make_order(db, other_profile.id, order_status="completed")
    other_item = await _make_order_item(db, other_order.id, variant)

    await client.post("/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user))
    await client.post("/return-requests", json={"order_item_id": other_item.id}, headers=auth_headers(other))

    response = await client.get("/return-requests", headers=auth_headers(user))

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["order_item_id"] == item.id


# ---- Return Requests: status update (staff-only) ----

@pytest.mark.asyncio
async def test_update_return_request_status_as_staff(
    client: AsyncClient, db: AsyncSession, make_customer, make_staff, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user5@example.com")
    staff, _ = await make_staff()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved", "refund_amount": 20.00},
        headers=auth_headers(staff),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "approved"
    assert body["refund_amount"] == 20.00
    assert body["processed_at"] is not None


@pytest.mark.asyncio
async def test_update_return_request_status_as_customer_forbidden(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user6@example.com")
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved"},
        headers=auth_headers(user),
    )

    assert response.status_code == 403


@pytest.mark.asyncio
async def test_update_return_request_status_not_found(client: AsyncClient, make_staff, auth_headers):
    staff, _ = await make_staff()

    response = await client.patch(
        "/return-requests/999999/status",
        json={"status": "approved"},
        headers=auth_headers(staff),
    )

    assert response.status_code == 404
````

## File: backend/tests/test_customer_profiles.py
````python
import pytest

pytestmark = pytest.mark.asyncio


async def test_get_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileget@example.com")
    headers = auth_headers(user)

    resp = await client.get("/me", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["email"] == "profileget@example.com"
    assert body["id"] == user.id


async def test_get_profile_unauthenticated(client):
    resp = await client.get("/me")
    assert resp.status_code == 401


async def test_get_profile_invalid_token(client):
    resp = await client.get("/me", headers={"Authorization": "Bearer not-a-real-token"})
    assert resp.status_code == 401


async def test_update_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileupdate@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"name": "Updated Name"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "Updated Name"


async def test_update_profile_partial_fields_unchanged(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profilepartial@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"phone_number": "+19998887777"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["phone_number"] == "+19998887777"
    assert body["name"] == "Test Customer"


async def test_update_profile_unauthenticated(client):
    resp = await client.put("/me", json={"name": "Nope"})
    assert resp.status_code == 401


async def test_list_addresses_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/addresses", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_create_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrcreate@example.com")
    headers = auth_headers(user)

    payload = {
        "country": "USA",
        "state": "CA",
        "city": "Los Angeles",
        "postal_code": "90001",
        "address_line_1": "123 Main St",
        "address_line_2": None,
        "is_default": True,
    }
    resp = await client.post("/addresses", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["city"] == "Los Angeles"
    assert body["is_default"] is True


async def test_create_address_unauthenticated(client):
    payload = {
        "country": "USA",
        "city": "Los Angeles",
        "address_line_1": "123 Main St",
    }
    resp = await client.post("/addresses", json=payload)
    assert resp.status_code == 401


async def test_create_second_default_address_unsets_first(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdefault@example.com")
    headers = auth_headers(user)

    first_payload = {
        "country": "USA",
        "city": "Austin",
        "address_line_1": "1 First St",
        "is_default": True,
    }
    first_resp = await client.post("/addresses", json=first_payload, headers=headers)
    assert first_resp.status_code == 201
    first_id = first_resp.json()["id"]

    second_payload = {
        "country": "USA",
        "city": "Dallas",
        "address_line_1": "2 Second St",
        "is_default": True,
    }
    second_resp = await client.post("/addresses", json=second_payload, headers=headers)
    assert second_resp.status_code == 201

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False


async def test_update_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdate@example.com")
    headers = auth_headers(user)

    create_payload = {
        "country": "USA",
        "city": "Denver",
        "address_line_1": "1 Old St",
    }
    create_resp = await client.post("/addresses", json=create_payload, headers=headers)
    address_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/addresses/{address_id}", json={"city": "Boulder"}, headers=headers
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["city"] == "Boulder"


async def test_update_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/addresses/999999", json={"city": "Nowhere"}, headers=headers)
    assert resp.status_code == 404


async def test_update_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrowner@example.com")
    intruder, _ = await make_customer(email="addrintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Miami", "address_line_1": "1 Owner St"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.put(
        f"/addresses/{address_id}",
        json={"city": "Hacked"},
        headers=auth_headers(intruder),
    )
    assert resp.status_code == 404


async def test_update_address_set_default_unsets_others(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatedefault@example.com")
    headers = auth_headers(user)

    first_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Seattle", "address_line_1": "1 A St", "is_default": True},
        headers=headers,
    )
    first_id = first_resp.json()["id"]

    second_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Portland", "address_line_1": "2 B St", "is_default": False},
        headers=headers,
    )
    second_id = second_resp.json()["id"]

    await client.put(f"/addresses/{second_id}", json={"is_default": True}, headers=headers)

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False
    assert addresses[second_id] is True


async def test_delete_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdelete@example.com")
    headers = auth_headers(user)

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Phoenix", "address_line_1": "1 Delete St"},
        headers=headers,
    )
    address_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/addresses/{address_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get("/addresses", headers=headers)
    assert all(a["id"] != address_id for a in list_resp.json())


async def test_delete_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/addresses/999999", headers=headers)
    assert resp.status_code == 404


async def test_delete_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrdelowner@example.com")
    intruder, _ = await make_customer(email="addrdelintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Tampa", "address_line_1": "1 Owner Ave"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.delete(f"/addresses/{address_id}", headers=auth_headers(intruder))
    assert resp.status_code == 404
````

## File: backend/tests/test_payments.py
````python
import json
import pytest
import stripe
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


class FakePaymentIntent:
    def __init__(self, client_secret="pi_test_secret_123"):
        self.client_secret = client_secret


async def test_create_intent_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paycreateintent@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=20.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=3)

    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        return FakePaymentIntent()

    monkeypatch.setattr(stripe.PaymentIntent, "create", fake_create)

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["client_secret"] == "pi_test_secret_123"
    assert captured["amount"] == 6000
    assert captured["currency"] == "usd"


async def test_create_intent_empty_cart(client, make_customer, auth_headers, monkeypatch):
    user, _ = await make_customer(email="paynocart@example.com")
    headers = auth_headers(user)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_create_intent_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinsufficientstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]


async def test_create_intent_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinactivevariant@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_create_intent_unauthenticated(client, monkeypatch):
    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())
    resp = await client.post("/payments/create-intent")
    assert resp.status_code == 401


async def test_webhook_invalid_payload(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise ValueError("bad payload")

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"not-real-json",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid payload"


async def test_webhook_invalid_signature(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise stripe.error.SignatureVerificationError("bad sig", sig_header)

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid signature"


async def test_webhook_payment_succeeded_creates_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhooksuccess@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=30.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=2)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    def fake_construct_event(payload, sig_header, secret):
        return fake_event

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    order = order_result.scalar_one_or_none()
    assert order is not None
    assert order.status == "paid"
    assert order.total_amount == 60.0

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_webhook_ignores_other_event_types(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookother@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.payment_failed",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    assert order_result.scalar_one_or_none() is None

    await db.refresh(variant)
    assert variant.stock_quantity == 10


async def test_webhook_missing_metadata_no_crash(client, monkeypatch):
    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {"object": {"metadata": {}}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200


async def test_webhook_retry_does_not_duplicate_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookretry@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    profile_id = profile.id

    variant = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile_id),
                }
            }
        },
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    first_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert first_resp.status_code == 200

    await db.refresh(profile)

    second_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert second_resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile_id))
    orders = order_result.scalars().all()
    assert len(orders) == 1
````

## File: backend/tests/test_reviews.py
````python
import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


async def test_get_product_reviews_empty(client, make_product_variant):
    variant = await make_product_variant()
    resp = await client.get(f"/products/{variant.product_id}/reviews")
    assert resp.status_code == 200
    assert resp.json() == []


async def test_get_product_reviews_product_not_found(client):
    resp = await client.get("/products/999999/reviews")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewcreate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 5, "comment": "Great product"}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Great product"
    assert body["product_id"] == product_id


async def test_create_review_product_not_found(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewproductnotfound@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, _ = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 4}
    resp = await client.post("/products/999999/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_order_item_not_found(client, make_customer, auth_headers, make_product_variant):
    user, _ = await make_customer(email="reviewitemnotfound@example.com")
    headers = auth_headers(user)

    variant = await make_product_variant()

    payload = {"order_item_id": 999999, "rating": 3}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Order item not found"


async def test_create_review_invalid_rating(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewinvalidrating@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 6}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 422


async def test_create_review_unauthenticated(client, make_product_variant):
    variant = await make_product_variant()
    payload = {"order_item_id": 1, "rating": 5}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload)
    assert resp.status_code == 401


async def test_get_product_reviews_after_creation(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewlistafter@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4, "comment": "Nice"},
        headers=headers,
    )

    resp = await client.get(f"/products/{product_id}/reviews")
    assert resp.status_code == 200
    body = resp.json()
    assert len(body) == 1
    assert body[0]["rating"] == 4


async def test_update_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewupdate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 2, "comment": "Meh"},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 5, "comment": "Actually great"}, headers=headers
    )
    assert update_resp.status_code == 200
    body = update_resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Actually great"


async def test_update_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/reviews/999999", json={"rating": 3}, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_update_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewowner@example.com")
    intruder, _ = await make_customer(email="reviewintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 5},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 1}, headers=auth_headers(intruder)
    )
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only edit your own reviews"


async def test_update_review_unauthenticated(client, make_customer, make_order_item, db):
    user, _ = await make_customer(email="reviewupdateunauth@example.com")
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    order_item, product_id = await make_order_item(profile.id)

    resp = await client.put("/reviews/1", json={"rating": 3})
    assert resp.status_code == 401


async def test_delete_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewdelete@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 3},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/reviews/{review_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get(f"/products/{product_id}/reviews")
    assert all(r["id"] != review_id for r in list_resp.json())


async def test_delete_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/reviews/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_delete_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewdelowner@example.com")
    intruder, _ = await make_customer(email="reviewdelintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.delete(f"/reviews/{review_id}", headers=auth_headers(intruder))
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only delete your own reviews"
````

## File: backend/tests/test_wishlist.py
````python
import pytest
from sqlalchemy import select

from app.models.product import Product

pytestmark = pytest.mark.asyncio


async def _make_product(db, name="Test Product"):
    product = Product(name=name, description="test", price=10.0)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def test_get_wishlist_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/wishlist", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_add_to_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistadd@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    resp = await client.post(
        "/wishlist",
        json={"product_id": product.id},
        headers=headers,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["product_id"] == product.id


async def test_add_to_wishlist_product_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistnotfound@example.com")
    headers = auth_headers(user)

    resp = await client.post(
        "/wishlist",
        json={"product_id": 999999},
        headers=headers,
    )
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_add_to_wishlist_duplicate(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistdup@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.post("/wishlist", json={"product_id": product.id}, headers=headers)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Product already in wishlist"


async def test_remove_from_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistremove@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.delete(f"/wishlist/{product.id}", headers=headers)

    assert resp.status_code == 204


async def test_remove_from_wishlist_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistremovenf@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/wishlist/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found in wishlist"
````

## File: backend/.dockerignore
````
__pycache__/
*.pyc
.venv/
venv/
.env
alembic/versions/__pycache__/
*.rar
*.zip
````

## File: backend/Dockerfile
````
FROM python:3.12-slim

WORKDIR /app

# System deps needed for psycopg2 / postgres client libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
````

## File: backend/pytest.ini
````ini
[pytest]
asyncio_mode = auto
testpaths = tests
````

## File: backend/requirements-dev.txt
````
aiosqlite==0.22.1
alembic==1.18.5
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.1
asyncpg==0.31.0
bcrypt==5.0.0
certifi==2026.7.22
cffi==2.0.0
charset-normalizer==3.4.9
click==8.4.2
colorama==0.4.6
coverage==7.15.2
cryptography==49.0.0
dnspython==2.8.0
ecdsa==0.19.2
email-validator==2.3.0
Faker==40.35.0
fastapi==0.139.0
greenlet==3.5.3
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.18
iniconfig==2.3.0
Mako==1.3.12
MarkupSafe==3.0.3
packaging==26.2
pluggy==1.6.0
psycopg==3.3.4
psycopg-binary==3.3.4
pyasn1==0.6.3
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.14.2
pydantic_core==2.46.4
Pygments==2.20.0
pytest==9.1.1
pytest-asyncio==1.4.0
pytest-cov==7.1.0
python-dotenv==1.2.2
python-jose==3.5.0
requests==2.34.2
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.51
starlette==1.3.1
stripe==15.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
tzdata==2026.2
urllib3==2.7.0
uvicorn==0.49.0
````

## File: frontend/.claude/rules/guardrails.md
````markdown
---
globs: "*"
---

# Core Project Configuration & Architecture

## Tech Stack

- Frontend Framework: Next.js (App Router, Version 15+)
- Language: TypeScript (Strict Type Checking)
- Styling: Tailwind CSS (Utility-first configuration)
- State Management: Zustand (Global Client-Side Stores)
- Form Handling: React Hook Form
- Validation: Zod (Schema validation for forms and API responses)
- Payments: Stripe (@stripe/stripe-js and @stripe/react-stripe-js)
- Backend: External FastAPI Backend Engine

## Folder Layout Structure

- `/app`: Pages, layouts, and route handlers.
- `/components`: Reusable global UI elements (buttons, inputs, modals).
- `/lib`: Modular code utilities.
- `/lib/api`: HTTP and WebSocket connection clients for FastAPI.
- `/lib/stores`: Zustand global state store modules.
- `/hooks`: Custom stateful React hooks.
- `/types`: Explicit TypeScript data interfaces and types.
- `/tests`: Unit, integration, and End-to-End test suites.

## Strict Production Guardrails

1. NO PLACEHOLDERS: Never output placeholders, partial modifications, or comments like `// TODO: Implement logic` or `// ... rest of code here`. Write out every file completely.
2. NO PROSE IN GENERATION: When acting as a code generator, skip conversational pleasantries, introductory text, and closing summaries. Output only the file path indicator followed by the raw code block.
3. ERROR HANDLING: Every API network operation and state transaction must be wrapped inside defensive `try/catch` processing blocks with strict user-facing fallback messages.
4. TYPE SAFETY: Avoid the use of `any` types. Every utility parameter, API response payload, and form state must be strictly declared with a definitive TypeScript interface or type.
5. BEST PRACTICES: Always follow elite, production-grade software engineering practices. Avoid quick fixes, lazy shortcuts, and architectural hacks. Write clean, modular, and highly scalable logic.
6. COMPREHENSIVE GUIDANCE: Do not give vague or high-level instructions. Instead of stating "make changes" or "write tests," explicitly guide step by step on how to execute those changes and write out the exact, actionable code blocks or testing logic required.
````

## File: frontend/.github/copilot-instructions.md
````markdown
---
globs: "*"
---

# Core Project Configuration & Architecture

## Tech Stack

- Frontend Framework: Next.js (App Router, Version 15+)
- Language: TypeScript (Strict Type Checking)
- Styling: Tailwind CSS (Utility-first configuration)
- State Management: Zustand (Global Client-Side Stores)
- Form Handling: React Hook Form
- Validation: Zod (Schema validation for forms and API responses)
- Payments: Stripe (@stripe/stripe-js and @stripe/react-stripe-js)
- Backend: External FastAPI Backend Engine

## Folder Layout Structure

- `/app`: Pages, layouts, and route handlers.
- `/components`: Reusable global UI elements (buttons, inputs, modals).
- `/lib`: Modular code utilities.
- `/lib/api`: HTTP and WebSocket connection clients for FastAPI.
- `/lib/stores`: Zustand global state store modules.
- `/hooks`: Custom stateful React hooks.
- `/types`: Explicit TypeScript data interfaces and types.
- `/tests`: Unit, integration, and End-to-End test suites.

## Strict Production Guardrails

1. NO PLACEHOLDERS: Never output placeholders, partial modifications, or comments like `// TODO: Implement logic` or `// ... rest of code here`. Write out every file completely.
2. NO PROSE IN GENERATION: When acting as a code generator, skip conversational pleasantries, introductory text, and closing summaries. Output only the file path indicator followed by the raw code block.
3. ERROR HANDLING: Every API network operation and state transaction must be wrapped inside defensive `try/catch` processing blocks with strict user-facing fallback messages.
4. TYPE SAFETY: Avoid the use of `any` types. Every utility parameter, API response payload, and form state must be strictly declared with a definitive TypeScript interface or type.
5. BEST PRACTICES: Always follow elite, production-grade software engineering practices. Avoid quick fixes, lazy shortcuts, and architectural hacks. Write clean, modular, and highly scalable logic.
6. COMPREHENSIVE GUIDANCE: Do not give vague or high-level instructions. Instead of stating "make changes" or "write tests," explicitly guide step by step on how to execute those changes and write out the exact, actionable code blocks or testing logic required.
````

## File: frontend/app/_(auth)/forgot-password/page.tsx
````typescript
export default function ForgotPasswordPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Forgot Password</h1>
        <p className="text-sm text-gray-600">
          Enter your email address to reset your account password.
        </p>
        {/* Form elements go here later */}
      </div>
    </div>
  );
}
````

## File: frontend/app/_(auth)/login/page.tsx
````typescript
export default function LoginPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Sign In</h1>
        <p className="text-sm text-gray-600">Welcome back! Please enter your details to log in.</p>
        {/* Login form code goes here later */}
      </div>
    </div>
  );
}
````

## File: frontend/app/_(auth)/register/page.tsx
````typescript
export default function RegisterPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Create an Account</h1>
        <p className="text-sm text-gray-600">
          Sign up today to manage your store and product logistics.
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/_(auth)/reset-password/page.tsx
````typescript
export default function ResetPasswordPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Reset Password</h1>
        <p className="text-sm text-gray-600">
          Please enter your new production password security credentials below.
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/_(auth)/verify-email/page.tsx
````typescript
export default function VerifyEmailPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Verify Email</h1>
        <p className="text-sm text-gray-600">
          We have sent a verification secure link to your registered email address.
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/_(auth)/layout.tsx
````typescript

````

## File: frontend/app/_(protected)/account/page.tsx
````typescript

````

## File: frontend/app/_(protected)/addresses/page.tsx
````typescript

````

## File: frontend/app/_(protected)/chat-history/page.tsx
````typescript

````

## File: frontend/app/_(protected)/checkout/order-confirmation/[orderId]/page.tsx
````typescript

````

## File: frontend/app/_(protected)/checkout/page.tsx
````typescript

````

## File: frontend/app/_(protected)/notifications/page.tsx
````typescript

````

## File: frontend/app/_(protected)/orders/[orderId]/return/page.tsx
````typescript

````

## File: frontend/app/_(protected)/orders/[orderId]/page.tsx
````typescript

````

## File: frontend/app/_(protected)/orders/page.tsx
````typescript

````

## File: frontend/app/_(protected)/profile/page.tsx
````typescript

````

## File: frontend/app/_(protected)/settings/page.tsx
````typescript

````

## File: frontend/app/_(protected)/wishlist/page.tsx
````typescript

````

## File: frontend/app/_(protected)/layout.tsx
````typescript

````

## File: frontend/app/_(public)/about/page.tsx
````typescript

````

## File: frontend/app/_(public)/cart/page.tsx
````typescript

````

## File: frontend/app/_(public)/categories/[slug]/page.tsx
````typescript

````

## File: frontend/app/_(public)/categories/page.tsx
````typescript

````

## File: frontend/app/_(public)/contact/page.tsx
````typescript

````

## File: frontend/app/_(public)/faq/page.tsx
````typescript

````

## File: frontend/app/_(public)/privacy/page.tsx
````typescript

````

## File: frontend/app/_(public)/products/[slug]/loading.tsx
````typescript

````

## File: frontend/app/_(public)/products/[slug]/page.tsx
````typescript

````

## File: frontend/app/_(public)/products/loading.tsx
````typescript

````

## File: frontend/app/_(public)/products/page.tsx
````typescript

````

## File: frontend/app/_(public)/return-policy/page.tsx
````typescript

````

## File: frontend/app/_(public)/search/page.tsx
````typescript

````

## File: frontend/app/_(public)/terms/page.tsx
````typescript

````

## File: frontend/app/_(public)/layout.tsx
````typescript

````

## File: frontend/app/_(public)/loading.tsx
````typescript

````

## File: frontend/app/_(public)/page.tsx
````typescript

````

## File: frontend/app/api/auth/login/route.ts
````typescript

````

## File: frontend/app/api/auth/logout/route.ts
````typescript

````

## File: frontend/app/api/checkout/create-payment-intent/route.ts
````typescript

````

## File: frontend/app/api/webhooks/stripe/route.ts
````typescript

````

## File: frontend/app/error.tsx
````typescript
"use client"; // Must be the absolute first line of code

import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-4 text-center">
      <h2 className="text-xl font-bold text-red-600">Something went wrong!</h2>
      <button
        onClick={() => reset()}
        className="mt-4 rounded bg-gray-900 px-4 py-2 text-sm font-medium text-white hover:bg-gray-800"
      >
        Try again
      </button>
    </div>
  );
}
````

## File: frontend/app/layout.tsx
````typescript
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "E-Commerce Storefront",
  description: "Production e-commerce frontend built on Next.js",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-white text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
````

## File: frontend/app/not-found.tsx
````typescript
import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4 text-center">
      <h1 className="text-6xl font-extrabold text-gray-900">404</h1>
      <h2 className="mt-4 text-xl font-bold text-gray-700">Page Not Found</h2>
      <p className="mt-2 text-base text-gray-500">
        Sorry, we couldn’t find the page you’re looking for.
      </p>
      <div className="mt-6">
        <Link
          href="/"
          className="inline-flex items-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-gray-800 focus:outline-none"
        >
          Go back home
        </Link>
      </div>
    </div>
  );
}
````

## File: frontend/app/robots.ts
````typescript
import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
  };
}
````

## File: frontend/app/sitemap.ts
````typescript
import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: "https://localhost:3000",
      lastModified: new Date(),
    },
  ];
}
````

## File: frontend/e2e/auth.spec.ts
````typescript

````

## File: frontend/e2e/checkout.spec.ts
````typescript

````

## File: frontend/e2e/phase1-checkpoint.spec.ts
````typescript

````

## File: frontend/hooks/useDebouncedValue.ts
````typescript

````

## File: frontend/hooks/useOrderStatusPolling.ts
````typescript

````

## File: frontend/hooks/useWebSocket.ts
````typescript

````

## File: frontend/lib/api/notifications.ts
````typescript

````

## File: frontend/lib/api/reviews.ts
````typescript

````

## File: frontend/lib/api/wishlist.ts
````typescript

````

## File: frontend/lib/stores/cartStore.ts
````typescript

````

## File: frontend/lib/stores/checkoutStore.ts
````typescript

````

## File: frontend/lib/stores/notificationStore.ts
````typescript

````

## File: frontend/lib/stores/wishlistStore.ts
````typescript

````

## File: frontend/lib/stripe/client.ts
````typescript

````

## File: frontend/lib/stripe/paymentIntent.ts
````typescript

````

## File: frontend/lib/utils/format.ts
````typescript

````

## File: frontend/lib/validation/contact.ts
````typescript

````

## File: frontend/lib/validation/review.ts
````typescript

````

## File: frontend/lib/websocket/chatConnection.ts
````typescript

````

## File: frontend/lib/websocket/connectionManager.ts
````typescript

````

## File: frontend/types/auth.ts
````typescript

````

## File: frontend/types/cart.ts
````typescript

````

## File: frontend/types/category.ts
````typescript

````

## File: frontend/types/chats.ts
````typescript

````

## File: frontend/types/notification.ts
````typescript

````

## File: frontend/types/review.ts
````typescript

````

## File: frontend/types/role.ts
````typescript

````

## File: frontend/types/wishlist.ts
````typescript

````

## File: frontend/.env.example
````
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_WS_URL=wss://ws.example.com
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_replace_me
````

## File: frontend/.prettierrc
````
{
  "semi": true,
  "singleQuote": false,
  "trailingComma": "es5",
  "tabWidth": 2,
  "printWidth": 100
}
````

## File: frontend/eslint.config.mjs
````javascript
import { FlatCompat } from "@eslint/eslintrc";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [...compat.extends("next/core-web-vitals", "next/typescript")];

export default eslintConfig;
````

## File: frontend/gitignore
````
node_modules
.next
.env.local
*.log
````

## File: frontend/jest.config.ts
````typescript
import type { Config } from "jest";

const config: Config = {
  preset: "ts-jest",
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/$1",
    "\\.(css|less|scss|sass)$": "identity-obj-proxy",
  },
  transform: {
    "^.+\\.(ts|tsx)$": ["ts-jest", { tsconfig: "tsconfig.jest.json" }],
  },
  testPathIgnorePatterns: ["/node_modules/", "/e2e/"],
};

export default config;
````

## File: frontend/jest.setup.ts
````typescript
import "@testing-library/jest-dom";

// Mock Next.js Navigation Router context hooks globally
jest.mock("next/navigation", () => ({
  useRouter: () => ({
    push: jest.fn(),
    replace: jest.fn(),
    prefetch: jest.fn(),
    back: jest.fn(),
    forward: jest.fn(),
    refresh: jest.fn(),
  }),
  usePathname: () => "/",
  useSearchParams: () => new URLSearchParams(),
}));

// Mock modern global browser matchMedia query compatibility
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: jest.fn().mockImplementation((query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});
````

## File: frontend/next.config.ts
````typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [],
  },
  typescript: {
    // Keeps ignoring type errors from empty files during this test phase
    ignoreBuildErrors: true,
  },
};

export default nextConfig;
````

## File: frontend/playwright.config.ts
````typescript
import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
});
````

## File: frontend/postcss.config.js
````javascript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
````

## File: frontend/PROGRESS.md
````markdown
# 🚀 Project Progress Status
*Last Synced: 2026-07-13 20:11:04*

## 📁 Current File Structure Map
```text
├── .env.example
├── .env.local
├── .prettierrc
├── app
│   ├── _(auth)
│   │   ├── forgot-password
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── login
│   │   │   └── page.tsx
│   │   ├── register
│   │   │   └── page.tsx
│   │   ├── reset-password
│   │   │   └── page.tsx
│   │   └── verify-email
│   │       └── page.tsx
│   ├── _(protected)
│   │   ├── account
│   │   │   └── page.tsx
│   │   ├── addresses
│   │   │   └── page.tsx
│   │   ├── chat-history
│   │   │   └── page.tsx
│   │   ├── checkout
│   │   │   ├── order-confirmation
│   │   │   │   └── [orderId]
│   │   │   │       └── page.tsx
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── notifications
│   │   │   └── page.tsx
│   │   ├── orders
│   │   │   ├── [orderId]
│   │   │   │   ├── page.tsx
│   │   │   │   └── return
│   │   │   │       └── page.tsx
│   │   │   └── page.tsx
│   │   ├── profile
│   │   │   └── page.tsx
│   │   ├── settings
│   │   │   └── page.tsx
│   │   └── wishlist
│   │       └── page.tsx
│   ├── _(public)
│   │   ├── about
│   │   │   └── page.tsx
│   │   ├── cart
│   │   │   └── page.tsx
│   │   ├── categories
│   │   │   ├── [slug]
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── contact
│   │   │   └── page.tsx
│   │   ├── faq
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── loading.tsx
│   │   ├── page.tsx
│   │   ├── privacy
│   │   │   └── page.tsx
│   │   ├── products
│   │   │   ├── [slug]
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── loading.tsx
│   │   │   └── page.tsx
│   │   ├── return-policy
│   │   │   └── page.tsx
│   │   ├── search
│   │   │   └── page.tsx
│   │   └── terms
│   │       └── page.tsx
│   ├── api
│   │   ├── auth
│   │   │   ├── login
│   │   │   │   └── route.ts
│   │   │   └── logout
│   │   │       └── route.ts
│   │   ├── checkout
│   │   │   └── create-payment-intent
│   │   │       └── route.ts
│   │   └── webhooks
│   │       └── stripe
│   │           └── route.ts
│   ├── error.tsx
│   ├── globals.css
│   ├── layout.tsx
│   ├── not-found.tsx
│   ├── page.tsx
│   ├── robots.ts
│   └── sitemap.ts
├── components
│   ├── features
│   │   ├── auth
│   │   ├── cart
│   │   ├── chat
│   │   ├── checkout
│   │   ├── notifications
│   │   ├── orders
│   │   ├── product
│   │   ├── reviews
│   │   ├── search
│   │   └── wishlist
│   ├── layout
│   └── ui
├── e2e
│   ├── auth.spec.ts
│   ├── checkout.spec.ts
│   └── phase1-checkpoint.spec.ts
├── eslint.config.mjs
├── gitignore
├── hooks
│   ├── useDebouncedValue.ts
│   ├── useOrderStatusPolling.ts
│   └── useWebSocket.ts
├── lib
│   ├── api
│   │   ├── auth.ts
│   │   ├── cart.ts
│   │   ├── client.ts
│   │   ├── notifications.ts
│   │   ├── orders.ts
│   │   ├── products.ts
│   │   ├── reviews.ts
│   │   ├── users.ts
│   │   └── wishlist.ts
│   ├── stores
│   │   ├── authStore.ts
│   │   ├── cartStore.ts
│   │   ├── checkoutStore.ts
│   │   ├── notificationStore.ts
│   │   └── wishlistStore.ts
│   ├── stripe
│   │   ├── client.ts
│   │   └── paymentIntent.ts
│   ├── utils
│   │   └── format.ts
│   ├── validation
│   │   ├── address.ts
│   │   ├── auth.ts
│   │   ├── contact.ts
│   │   └── review.ts
│   └── websocket
│       ├── chatConnection.ts
│       └── connectionManager.ts
├── next-env.d.ts
├── next.config.ts
├── package-lock.json
├── package.json
├── postcss.config.js
├── public
├── tests
│   └── smoke.test.tsx
├── tsconfig.json
└── types
    ├── api.ts
    ├── order.ts
    ├── product.ts
    └── user.ts
```

## ⏱️ Recently Modified Files (Active Workspace Delta)
- `types\user.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\product.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\order.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\api.ts` *(Modified: 2026-07-13 17:05:11)*
- `tsconfig.json` *(Modified: 2026-07-13 18:59:31)*

## 📝 Next Steps / Tasks to Do
- [ ] Build lib/api/ with a typed client for auth, products, orders, users, cart resources.
````

## File: frontend/tsconfig.jest.json
````json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "module": "commonjs",
    "moduleResolution": "node",
    "jsx": "react-jsx",
    "esModuleInterop": true,
    "isolatedModules": true
  }
}
````

## File: frontend/update_progress.py
````python
import os
import time
from datetime import datetime

# Specific development file types and folder layers ignored by the mapping process
IGNORE_LIST = {
    '.git', '.claude', '.github', 'node_modules', '__pycache__', 
    'update_progress.py', 'PROGRESS.md', 'repomix-output.txt', '.next', 'dist'
}

def get_project_tree(dir_path, prefix=""):
    """Recursively calculates a visual text-based layout of directories and files."""
    tree = ""
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return ""
    
    # Filter out hidden deployment or asset directories
    items = [item for item in items if item not in IGNORE_LIST]
    
    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        tree += f"{prefix}{connector}{item}\n"
        
        if os.path.isdir(path):
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree += get_project_tree(path, next_prefix)
    return tree

def get_recent_files(dir_path, limit=5):
    """Identifies and indexes the most recently updated project code files."""
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        # Skip evaluating ignored system directory paths
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        for file in files:
            if file in IGNORE_LIST:
                continue
            path = os.path.join(root, file)
            try:
                mod_time = os.path.getmtime(path)
                file_list.append((path, mod_time))
            except FileNotFoundError:
                continue
                
    # Sort paths descending by date modified
    file_list.sort(key=lambda x: x, reverse=True)
    return file_list[:limit]

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("⏳ Analyzing project structure and identifying current development delta...")
    
    folder_tree = get_project_tree(root_dir)
    recent_files = get_recent_files(root_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown_content = f"""# 🚀 Project Progress Status
*Last Synced: {timestamp}*

## 📁 Current File Structure Map
```text
{folder_tree if folder_tree else 'Project root is currently clear.'}```

## ⏱️ Recently Modified Files (Active Workspace Delta)
"""
    if recent_files:
        for path, mod_time in recent_files:
            relative_path = os.path.relpath(path, root_dir)
            readable_time = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            markdown_content += f"- `{relative_path}` *(Modified: {readable_time})*\n"
    else:
        markdown_content += "- No recent modifications detected in this work session.\n"
        
    markdown_content += """
## 📝 Next Steps / Tasks to Do
- [ ] *Insert your active architectural prompt or next component requirement here*
"""

    with open(os.path.join(root_dir, "PROGRESS.md"), "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print("✅ PROGRESS.md documentation block compiled successfully.")

if __name__ == "__main__":
    main()
````

## File: package.json
````json
{
  "devDependencies": {
    "@tailwindcss/postcss": "^4.3.2"
  }
}
````

## File: backend/alembic/env.py
````python
from logging.config import fileConfig
import os

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context

load_dotenv()  # loads variables from backend/.env into os.environ

config = context.config

# Override sqlalchemy.url from the DATABASE_URL environment variable
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")
config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from app.database.base import Base
from app.models import *  # This pulls in every model registered in __init__.py
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
````

## File: backend/app/api/routes/checkout.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.order import OrderOut
from app.core.auth import get_current_user

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.post("/checkout", response_model=OrderOut, status_code=201)
async def checkout(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Lock and validate stock for every line before committing anything
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )

    new_order = Order(
        customer_id=profile.id,
        order_status="open",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()  # assigns new_order.id without committing

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one()

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in cart.items:
        await db.delete(item)

    await db.commit()

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == new_order.id)
    )
    return result.scalar_one()
````

## File: backend/app/api/routes/customer_auth.py
````python
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_auth import (
    CustomerRegisterRequest,
    CustomerRegisterResponse,
    CustomerLoginRequest,
    CustomerToken,
    CustomerRefreshRequest,
    CustomerVerifyEmailRequest,
    CustomerResendVerificationRequest,
    CustomerForgotPasswordRequest,
    CustomerResetPasswordRequest,
    MsgResponse,
)
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token, create_refresh_token
from app.core.email import send_verification_email, send_password_reset_email

router = APIRouter(prefix="/customer/auth", tags=["Customer Auth"])

CUSTOMER_ROLE_ID = 4
VERIFICATION_TOKEN_EXPIRE_HOURS = 24
RESET_TOKEN_EXPIRE_HOURS = 1


def _issue_tokens(user: User) -> CustomerToken:
    access_token = create_access_token(
        {"sub": str(user.id), "email": user.email, "role_id": user.role_id}
    )
    refresh_token, refresh_expires_at = create_refresh_token()
    user.refresh_token = refresh_token
    user.refresh_token_expires_at = refresh_expires_at
    return CustomerToken(access_token=access_token, refresh_token=refresh_token, token_type="bearer")


@router.post("/register", response_model=CustomerRegisterResponse, status_code=status.HTTP_201_CREATED)
async def customer_register(payload: CustomerRegisterRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    verification_token = secrets.token_urlsafe(32)

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        role_id=CUSTOMER_ROLE_ID,
        is_active=True,
        email_verified=False,
        email_verification_token=verification_token,
        email_verification_expires_at=datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS),
    )
    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Could not create account")

    await db.refresh(new_user)

    profile = CustomerProfile(user_id=new_user.id)
    db.add(profile)
    await db.commit()

    send_verification_email(new_user.email, verification_token)

    return CustomerRegisterResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email,
        email_verified=new_user.email_verified,
        message="Account created. Check your email to verify your account.",
    )


@router.post("/login", response_model=CustomerToken)
async def customer_login(payload: CustomerLoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or user.role_id != CUSTOMER_ROLE_ID:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not verify_password(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is inactive")

    token = _issue_tokens(user)
    await db.commit()

    return token


@router.post("/refresh", response_model=CustomerToken)
async def customer_refresh(payload: CustomerRefreshRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.refresh_token == payload.refresh_token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    if not user.refresh_token_expires_at or user.refresh_token_expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is inactive")

    token = _issue_tokens(user)  # rotates refresh token
    await db.commit()

    return token


@router.post("/logout", response_model=MsgResponse)
async def customer_logout(payload: CustomerRefreshRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.refresh_token == payload.refresh_token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        user.refresh_token = None
        user.refresh_token_expires_at = None
        await db.commit()

    return MsgResponse(message="Logged out successfully.")


@router.post("/verify-email", response_model=MsgResponse)
async def customer_verify_email(payload: CustomerVerifyEmailRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email_verification_token == payload.token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    if (
        not user.email_verification_expires_at
        or user.email_verification_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    user.email_verified = True
    user.email_verification_token = None
    user.email_verification_expires_at = None
    await db.commit()

    return MsgResponse(message="Email verified successfully. You can now log in.")


@router.post("/resend-verification", response_model=MsgResponse)
async def customer_resend_verification(payload: CustomerResendVerificationRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists and is unverified, a new link has been sent.")

    if not user or user.email_verified:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.email_verification_token = token
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_verification_email(user.email, token)

    return generic_response


@router.post("/forgot-password", response_model=MsgResponse)
async def customer_forgot_password(payload: CustomerForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists, a password reset link has been sent.")

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def customer_reset_password(payload: CustomerResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if (
        not user.password_reset_expires_at
        or user.password_reset_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(message="Password reset successfully. Please log in with your new password.")
````

## File: backend/app/api/routes/customer_order.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.models.customer_order import Order, OrderItem, ReturnRequest
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_order import (
    CustomerOrderOut,
    ReturnRequestCreate,
    ReturnRequestStatusUpdate,
    ReturnRequestOut,
)
from app.core.auth import get_current_user
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter(tags=["Customer Orders"])

CANCELLABLE_STATUSES = {"open", "pending"}


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_own_order(db: AsyncSession, order_id: int, profile: CustomerProfile) -> Order:
    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
    )
    order = result.scalar_one_or_none()
    if not order or order.customer_id != profile.id:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# ---- Orders ----

@router.post("/orders/{order_id}/cancel", response_model=CustomerOrderOut)
async def cancel_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)

    if order.order_status not in CANCELLABLE_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Order in status '{order.order_status}' cannot be cancelled",
        )

    order.order_status = "cancelled"
    await db.commit()
    order = await _get_own_order(db, order_id, profile)
    return order


@router.post("/orders/{order_id}/reorder", response_model=CustomerOrderOut, status_code=201)
async def reorder(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    old_order = await _get_own_order(db, order_id, profile)

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(customer_id=profile.id)
        db.add(cart)
        await db.flush()

    for old_item in old_order.items:
        if old_item.product_variant_id is None:
            continue
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == cart.id,
                CartItem.product_variant_id == old_item.product_variant_id,
            )
        )
        cart_item = result.scalar_one_or_none()
        if cart_item:
            cart_item.quantity += old_item.quantity
        else:
            db.add(CartItem(
                cart_id=cart.id,
                product_variant_id=old_item.product_variant_id,
                quantity=old_item.quantity,
            ))

    await db.commit()
    old_order = await _get_own_order(db, order_id, profile)
    return old_order


@router.get("/orders/{order_id}/invoice", response_model=CustomerOrderOut)
async def get_invoice(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)
    return order


# ---- Return Requests ----

@router.post("/return-requests", response_model=ReturnRequestOut, status_code=status.HTTP_201_CREATED)
async def create_return_request(
    payload: ReturnRequestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(OrderItem).join(Order, Order.id == OrderItem.order_id).where(
            OrderItem.id == payload.order_item_id,
            Order.customer_id == profile.id,
        )
    )
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    existing = await db.execute(
        select(ReturnRequest).where(ReturnRequest.order_item_id == payload.order_item_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Return request already exists for this item")

    return_request = ReturnRequest(
        order_item_id=payload.order_item_id,
        customer_id=profile.id,
        reason=payload.reason,
    )
    db.add(return_request)
    await db.commit()
    await db.refresh(return_request)
    return return_request


@router.get("/return-requests", response_model=list[ReturnRequestOut])
async def list_return_requests(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(ReturnRequest).where(ReturnRequest.customer_id == profile.id)
    )
    return result.scalars().all()


@router.patch("/return-requests/{request_id}/status", response_model=ReturnRequestOut)
async def update_return_request_status(
    request_id: int,
    payload: ReturnRequestStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF)),
):
    result = await db.execute(select(ReturnRequest).where(ReturnRequest.id == request_id))
    return_request = result.scalar_one_or_none()
    if not return_request:
        raise HTTPException(status_code=404, detail="Return request not found")

    return_request.status = payload.status
    if payload.refund_amount is not None:
        return_request.refund_amount = payload.refund_amount
    if payload.status in ("approved", "rejected", "completed"):
        from datetime import datetime, timezone
        return_request.processed_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(return_request)
    return return_request
````

## File: backend/app/api/routes/permissions.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.permission import Permission
from app.models.user import User
from app.schemas.permission import PermissionOut, PermissionCreate, PermissionUpdate
from app.core.permissions import require_role, ADMIN

router = APIRouter()


@router.get("/permissions", response_model=list[PermissionOut])
async def get_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/permissions/{permission_id}", response_model=PermissionOut)
async def get_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.post("/permissions", response_model=PermissionOut, status_code=201)
async def create_permission(
    payload: PermissionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Permission name already exists")

    new_permission = Permission(name=payload.name, description=payload.description)
    db.add(new_permission)
    await db.commit()
    await db.refresh(new_permission)
    return new_permission


@router.put("/permissions/{permission_id}", response_model=PermissionOut)
async def update_permission(
    permission_id: int,
    payload: PermissionUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(permission, field, value)

    await db.commit()
    await db.refresh(permission)
    return permission


@router.delete("/permissions/{permission_id}", status_code=204)
async def delete_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    await db.delete(permission)
    await db.commit()
    return None
````

## File: backend/app/api/routes/product_categories.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.category import Category
from app.models.product_category import ProductCategory
from app.models.user import User
from app.schemas.product_category import ProductCategoryOut, ProductCategoryCreate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/categories", response_model=list[ProductCategoryOut])
async def get_product_categories(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductCategory).where(ProductCategory.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/categories", response_model=ProductCategoryOut, status_code=201)
async def assign_category_to_product(
    product_id: int,
    payload: ProductCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Category).where(Category.id == payload.category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == payload.category_id,
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="This product is already assigned to this category")

    link = ProductCategory(product_id=product_id, category_id=payload.category_id)
    db.add(link)
    await db.commit()
    await db.refresh(link)
    return link


@router.delete("/products/{product_id}/categories/{category_id}", status_code=204)
async def remove_category_from_product(
    product_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == category_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="This product is not assigned to this category")

    await db.delete(link)
    await db.commit()
    return None
````

## File: backend/app/api/routes/product_variants.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.product_variant import ProductVariantOut, ProductVariantCreate, ProductVariantUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/variants", response_model=list[ProductVariantOut])
async def get_product_variants(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductVariant).where(ProductVariant.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/variants", response_model=ProductVariantOut, status_code=201)
async def create_product_variant(
    product_id: int,
    payload: ProductVariantCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_variant = ProductVariant(
        product_id=product_id,
        sku=payload.sku,
        price=payload.price,
        stock_quantity=payload.stock_quantity,
        is_active=payload.is_active,
    )
    db.add(new_variant)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(new_variant)
    return new_variant


@router.get("/variants/{variant_id}", response_model=ProductVariantOut)
async def get_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")
    return variant


@router.put("/variants/{variant_id}", response_model=ProductVariantOut)
async def update_variant(
    variant_id: int,
    payload: ProductVariantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(variant, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(variant)
    return variant


@router.delete("/variants/{variant_id}", status_code=204)
async def delete_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    try:
        await db.delete(variant)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="This variant cannot be deleted because it has existing orders. Deactivate it instead.",
        )

    return None
````

## File: backend/app/api/routes/products.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductOut, ProductCreate, ProductUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products", response_model=list[ProductOut])
async def get_products(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product))
    return result.scalars().all()


@router.get("/products/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(
    payload: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Product name already exists")

    new_product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        is_active=payload.is_active,
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)
    return product


@router.delete("/products/{product_id}", status_code=204)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(product)
    await db.commit()
    return None
````

## File: backend/app/api/routes/role_permissions.py
````python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.models.user import User
from app.schemas.permission import PermissionOut
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


class RolePermissionsSync(BaseModel):
    permission_ids: list[int]


@router.get("/roles/permissions", response_model=list[PermissionOut])
async def get_all_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/roles/{role_id}/permissions", response_model=list[PermissionOut])
async def get_role_permissions(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    result = await db.execute(
        select(Permission)
        .join(RolePermission, Permission.id == RolePermission.permission_id)
        .where(RolePermission.role_id == role_id)
    )
    return result.scalars().all()


@router.post("/roles/{role_id}/permissions", status_code=200)
async def assign_permissions_to_role(
    role_id: int,
    payload: RolePermissionsSync,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(select(RolePermission).where(RolePermission.role_id == role_id))
    current_links = result.scalars().all()
    current_perm_ids = {link.permission_id for link in current_links}

    target_perm_ids = set(payload.permission_ids)
    to_delete = [link for link in current_links if link.permission_id not in target_perm_ids]
    to_insert_ids = target_perm_ids - current_perm_ids

    for link in to_delete:
        await db.delete(link)

    if to_insert_ids:
        result = await db.execute(select(func.count()).select_from(Permission).where(Permission.id.in_(to_insert_ids)))
        valid_perms_count = result.scalar_one()
        if valid_perms_count != len(to_insert_ids):
            raise HTTPException(status_code=400, detail="One or more permission IDs are invalid")

        for perm_id in to_insert_ids:
            new_link = RolePermission(role_id=role_id, permission_id=perm_id)
            db.add(new_link)

    await db.commit()
    return {"status": "success", "message": "Permissions updated successfully"}


@router.delete("/roles/{role_id}/permissions/{permission_id}", status_code=204)
async def remove_permission_from_role(
    role_id: int,
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(
        select(RolePermission).where(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="Permission assignment not found")

    await db.delete(link)
    await db.commit()
    return None
````

## File: backend/app/api/routes/roles.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleOut, RoleCreate, RoleUpdate
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


@router.get("/roles", response_model=list[RoleOut])
async def get_roles(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role))
    return result.scalars().all()


@router.get("/roles/{role_id}", response_model=RoleOut)
async def get_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/roles", response_model=RoleOut, status_code=201)
async def create_role(
    payload: RoleCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Role name already exists")

    new_role = Role(name=payload.name, description=payload.description)
    db.add(new_role)
    await db.commit()
    await db.refresh(new_role)
    return new_role


@router.put("/roles/{role_id}", response_model=RoleOut)
async def update_role(
    role_id: int,
    payload: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(role, field, value)

    await db.commit()
    await db.refresh(role)
    return role


@router.delete("/roles/{role_id}", status_code=204)
async def delete_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    try:
        await db.delete(role)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Cannot delete role: it is still assigned to one or more users"
        )
    return None
````

## File: backend/app/core/jwt.py
````python
import secrets
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status

from app.core.config import settings

REFRESH_TOKEN_EXPIRE_DAYS = 7


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token() -> tuple[str, datetime]:
    token = secrets.token_urlsafe(64)
    expires_at = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    return token, expires_at


def verify_access_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
````

## File: backend/app/database/session.py
````python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Create our asynchronous database engine using modern Asyncio wrappers
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Shows SQL queries in terminal (disable in production)
    future=True
)

# Create an asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# Database Dependency - Yields an AsyncSession instead of a synchronous Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
````

## File: backend/app/models/category.py
````python
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/order_item.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int | None] = mapped_column(ForeignKey("product_variants.id", ondelete="SET NULL"), nullable=True)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_at_purchase: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    discount_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    order: Mapped["Order"] = relationship(back_populates="items")
    variant: Mapped["ProductVariant | None"] = relationship()
````

## File: backend/app/schemas/auth.py
````python
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
````

## File: backend/app/schemas/category.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CategoryOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
````

## File: backend/app/schemas/customer_auth.py
````python
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class CustomerRegisterRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: str | None = None


class CustomerRegisterResponse(BaseModel):
    id: int
    name: str
    email: str
    email_verified: bool
    message: str


class CustomerLoginRequest(BaseModel):
    email: EmailStr
    password: str


class CustomerToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class CustomerRefreshRequest(BaseModel):
    refresh_token: str


class CustomerVerifyEmailRequest(BaseModel):
    token: str


class CustomerResendVerificationRequest(BaseModel):
    email: EmailStr


class CustomerForgotPasswordRequest(BaseModel):
    email: EmailStr


class CustomerResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)


class MsgResponse(BaseModel):
    message: str
````

## File: backend/app/schemas/customer_order.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemOut


class CustomerOrderOut(BaseModel):
    id: int
    customer_name: str | None = None
    order_status: str
    total_amount: float
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class ReturnRequestCreate(BaseModel):
    order_item_id: int
    reason: str | None = Field(default=None, max_length=1000)


class ReturnRequestStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
    refund_amount: float | None = None


class ReturnRequestOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_item_id: int
    customer_id: int
    reason: str | None = None
    status: str
    refund_amount: float | None = None
    requested_at: datetime
    processed_at: datetime | None = None
````

## File: backend/app/schemas/user.py
````python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.role import RoleOut


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    role: RoleOut
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone_number: str | None = None
    avatar_url: str | None = None
    role_id: int | None = None
    is_active: bool | None = None
````

## File: backend/alembic.ini
````ini
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file. Left unset intentionally — env.py loads DATABASE_URL from .env via pydantic-settings/os.environ.
# sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
````

## File: frontend/app/globals.css
````css
@import "tailwindcss";

@theme {
  /* Brand Theme Tokens (Tailwind v4 standard configuration syntax) */
  --color-primary: #0f172a;
  --color-secondary: #475569;

  /* The engine automatically scans app/, components/, hooks/, etc. natively */
}
````

## File: frontend/app/page.tsx
````typescript
import React from "react";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <div className="max-w-md w-full bg-white shadow-md rounded-lg p-8 border border-gray-200">
        <h1 className="text-2xl font-bold text-gray-900 mb-2">E-commerce Storefront</h1>
        <p className="text-gray-600 mb-4">
          Welcome to the Next.js automated code factory enterprise web store instance.
        </p>
        <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors">
          Browse Products
        </button>
      </div>
    </main>
  );
}
````

## File: frontend/lib/api/cart.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, CartResponseData } from "@/types/api";

const FALLBACK_MESSAGES = {
  get: "We couldn't load your cart right now. Please refresh and try again.",
  add: "We couldn't add that item to your cart. Please try again.",
  update: "We couldn't update that item's quantity. Please try again.",
  remove: "We couldn't remove that item from your cart. Please try again.",
  clear: "We couldn't clear your cart. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getCart(signal?: AbortSignal): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.get<ApiResponse<CartResponseData>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.get);
  }
}

export async function addToCart(
  productId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.post<ApiResponse<CartResponseData>>(
      "/cart/items",
      { productId, quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.add);
  }
}

export async function updateCartItem(
  itemId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.put<ApiResponse<CartResponseData>>(
      `/cart/items/${itemId}`,
      { quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.update);
  }
}

export async function removeCartItem(
  itemId: string,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.delete<ApiResponse<CartResponseData>>(`/cart/items/${itemId}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.remove);
  }
}

export async function clearCart(signal?: AbortSignal): Promise<ApiResponse<null>> {
  try {
    return await apiClient.delete<ApiResponse<null>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.clear);
  }
}
````

## File: frontend/lib/api/client.ts
````typescript
import { ApiErrorResponse } from "@/types/api";

export type ApiErrorType = "http" | "parse" | "network" | "abort";

export class ApiError extends Error {
  status: number;
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null;
  errorType: ApiErrorType;

  constructor(
    status: number,
    message: string,
    errorType: ApiErrorType,
    detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null = null
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.errorType = errorType;
    this.detail = detail;
  }
}

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";
const DEFAULT_TIMEOUT_MS = 15000;

let refreshPromise: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  if (refreshPromise) {
    return refreshPromise;
  }

  refreshPromise = (async () => {
    const response = await fetch(`${BASE_URL}/auth/refresh`, {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new ApiError(response.status, "Session expired. Please log in again.", "http");
    }

    const data = (await response.json()) as { data?: { accessToken?: string } };
    const accessToken = data?.data?.accessToken;

    if (!accessToken) {
      throw new ApiError(500, "Session refresh failed. Please log in again.", "parse");
    }

    return accessToken;
  })();

  try {
    return await refreshPromise;
  } finally {
    refreshPromise = null;
  }
}

interface RequestOptions extends RequestInit {
  timeoutMs?: number;
  signal?: AbortSignal;
  skipAuthRetry?: boolean;
}

async function parseResponseBody(response: Response): Promise<unknown> {
  const contentType = response.headers.get("Content-Type");
  const isJson = contentType !== null && contentType.includes("application/json");
  const rawText = await response.text();

  if (rawText.length === 0) {
    return null;
  }

  if (isJson) {
    try {
      return JSON.parse(rawText);
    } catch {
      throw new ApiError(
        response.status,
        "The server returned a malformed response. Please try again.",
        "parse"
      );
    }
  }

  return rawText;
}

async function request<T>(endpoint: string, options: RequestOptions = {}): Promise<T> {
  const {
    timeoutMs = DEFAULT_TIMEOUT_MS,
    signal: externalSignal,
    skipAuthRetry,
    ...init
  } = options;

  const url = `${BASE_URL}${endpoint}`;

  const headers = new Headers(init.headers);
  if (!(init.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const timeoutController = new AbortController();
  const timeoutId = setTimeout(() => timeoutController.abort(), timeoutMs);

  const onExternalAbort = () => timeoutController.abort();
  if (externalSignal) {
    if (externalSignal.aborted) {
      timeoutController.abort();
    } else {
      externalSignal.addEventListener("abort", onExternalAbort);
    }
  }

  const config: RequestInit = {
    ...init,
    headers,
    credentials: "include",
    signal: timeoutController.signal,
  };

  try {
    let response: Response;
    try {
      response = await fetch(url, config);
    } catch (fetchError) {
      if (fetchError instanceof DOMException && fetchError.name === "AbortError") {
        if (externalSignal?.aborted) {
          throw new ApiError(0, "Request was cancelled.", "abort");
        }
        throw new ApiError(0, "The request timed out. Please try again.", "network");
      }
      throw new ApiError(0, "Unable to reach the server. Check your connection.", "network");
    }

    if (response.status === 204) {
      return {} as T;
    }

    if (response.status === 401 && !skipAuthRetry && endpoint !== "/auth/refresh") {
      try {
        await refreshAccessToken();
      } catch {
        throw new ApiError(401, "Your session has expired. Please log in again.", "http");
      }
      return request<T>(endpoint, { ...options, skipAuthRetry: true });
    }

    const responseData = await parseResponseBody(response);

    if (!response.ok) {
      const errorData = responseData as ApiErrorResponse | null;
      let errorMessage = "An unexpected error occurred. Please try again.";

      if (errorData && typeof errorData.detail === "string") {
        errorMessage = errorData.detail;
      } else if (errorData && Array.isArray(errorData.detail)) {
        errorMessage = errorData.detail.map((err) => `${err.loc.join(".")}: ${err.msg}`).join(", ");
      } else if (errorData && errorData.message) {
        errorMessage = errorData.message;
      }

      throw new ApiError(response.status, errorMessage, "http", errorData?.detail ?? null);
    }

    return responseData as T;
  } finally {
    clearTimeout(timeoutId);
    if (externalSignal) {
      externalSignal.removeEventListener("abort", onExternalAbort);
    }
  }
}

export const apiClient = {
  get: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "GET" }),
  post: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "POST",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  put: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PATCH",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  delete: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "DELETE" }),
};
````

## File: frontend/lib/api/orders.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, OrderQueryParams } from "@/types/api";
import { Order } from "@/types/order";

const FALLBACK_MESSAGES = {
  getOrders: "We couldn't load your orders right now. Please try again.",
  getOrderById: "We couldn't load that order right now. Please try again.",
  createOrder: "We couldn't place your order. Please try again.",
  cancelOrder: "We couldn't cancel that order. Please try again.",
  requestOrderReturn: "We couldn't submit your return request. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getOrders(
  params?: OrderQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Order>>> {
  try {
    const searchParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          searchParams.append(key, String(value));
        }
      });
    }
    const query = searchParams.toString() ? `?${searchParams.toString()}` : "";
    return await apiClient.get<ApiResponse<PaginatedResponse<Order>>>(`/orders${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrders);
  }
}

export async function getOrderById(
  orderId: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.get<ApiResponse<Order>>(`/orders/${orderId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrderById);
  }
}

export async function createOrder(
  orderData: {
    addressId: string;
    paymentIntentId: string;
  },
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>("/orders", orderData, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createOrder);
  }
}

export async function cancelOrder(
  orderId: string,
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/cancel`,
      { reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.cancelOrder);
  }
}

export async function requestOrderReturn(
  orderId: string,
  itemIds: string[],
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/return`,
      { itemIds, reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.requestOrderReturn);
  }
}
````

## File: frontend/lib/api/products.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, ProductQueryParams } from "@/types/api";
import { Product } from "@/types/product";

const FALLBACK_MESSAGES = {
  getProducts: "We couldn't load products right now. Please try again.",
  getProductBySlug: "We couldn't load that product right now. Please try again.",
  getProductById: "We couldn't load that product right now. Please try again.",
  getCategories: "We couldn't load product categories right now. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getProducts(
  params?: ProductQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Product>>> {
  try {
    const searchParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          searchParams.append(key, String(value));
        }
      });
    }
    const query = searchParams.toString() ? `?${searchParams.toString()}` : "";
    return await apiClient.get<ApiResponse<PaginatedResponse<Product>>>(`/products${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProducts);
  }
}

export async function getProductBySlug(
  slug: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/slug/${slug}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductBySlug);
  }
}

export async function getProductById(
  id: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/${id}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductById);
  }
}

export async function getCategories(signal?: AbortSignal): Promise<ApiResponse<string[]>> {
  try {
    return await apiClient.get<ApiResponse<string[]>>("/products/categories", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getCategories);
  }
}
````

## File: frontend/lib/stores/authStore.ts
````typescript
import { create } from "zustand";
import { persist } from "zustand/middleware";
import * as authApi from "@/lib/api/auth";
import { CustomerProfile } from "@/types/user";
import { LoginSchemaType, RegisterSchemaType } from "@/lib/validation/auth";

interface AuthState {
  accessToken: string | null;
  refreshToken: string | null;
  user: CustomerProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;

  login: (credentials: LoginSchemaType) => Promise<void>;
  register: (data: RegisterSchemaType) => Promise<void>;
  logout: () => Promise<void>;
  refreshAccessToken: () => Promise<string>;
  setUser: (user: CustomerProfile) => void;
  clearAuth: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set: (partial: Partial<AuthState>) => void, get: () => AuthState) => ({
      accessToken: null,
      refreshToken: null,
      user: null,
      isAuthenticated: false,
      isLoading: false,

      login: async (credentials: LoginSchemaType) => {
        set({ isLoading: true });
        try {
          const token = await authApi.login(credentials);
          set({
            accessToken: token.accessToken,
            refreshToken: token.refreshToken,
            isAuthenticated: true,
            isLoading: false,
          });
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      register: async (data: RegisterSchemaType) => {
        set({ isLoading: true });
        try {
          await authApi.register(data);
          set({ isLoading: false });
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      logout: async () => {
        const { refreshToken } = get();
        if (refreshToken) {
          try {
            await authApi.logout(refreshToken);
          } catch {
            // Ignore failures — clear local state regardless.
          }
        }
        get().clearAuth();
      },

      refreshAccessToken: async () => {
        const { refreshToken } = get();
        if (!refreshToken) {
          get().clearAuth();
          throw new Error("No refresh token available");
        }
        try {
          const token = await authApi.refreshToken(refreshToken);
          set({
            accessToken: token.accessToken,
            refreshToken: token.refreshToken,
            isAuthenticated: true,
          });
          return token.accessToken;
        } catch (error) {
          get().clearAuth();
          throw error;
        }
      },

      setUser: (user: CustomerProfile) => set({ user }),

      clearAuth: () =>
        set({
          accessToken: null,
          refreshToken: null,
          user: null,
          isAuthenticated: false,
        }),
    }),
    {
      name: "auth-storage",
      partialize: (state: AuthState) => ({
        accessToken: state.accessToken,
        refreshToken: state.refreshToken,
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
````

## File: frontend/lib/validation/address.ts
````typescript
import { z } from "zod";

export const addressSchema = z.object({
  title: z.string().min(1, "Address label title is required."),
  streetAddress: z.string().min(1, "Street address is required."),
  apartment: z.string().optional(),
  city: z.string().min(1, "City is required."),
  state: z.string().min(1, "State or province is required."),
  postalCode: z.string().min(1, "Postal code is required."),
  country: z.string().min(1, "Country name is required."),
  isDefault: z.boolean().default(false),
});

export type AddressSchemaType = z.infer<typeof addressSchema>;
````

## File: frontend/lib/validation/auth.ts
````typescript
import { z } from "zod";

export const loginSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
});

export const registerSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
  firstName: z.string().min(1, "First name is required."),
  lastName: z.string().min(1, "Last name is required."),
});

export const forgotPasswordSchema = z.object({
  email: z.string().email("Invalid email address format."),
});

export const resetPasswordSchema = z
  .object({
    token: z.string().min(1, "Reset token is required."),
    password: z.string().min(8, "Password must be at least 8 characters long."),
    confirmPassword: z.string().min(8, "Confirm password must be at least 8 characters long."),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords must match.",
    path: ["confirmPassword"],
  });

export type LoginSchemaType = z.infer<typeof loginSchema>;
export type RegisterSchemaType = z.infer<typeof registerSchema>;
export type ForgotPasswordSchemaType = z.infer<typeof forgotPasswordSchema>;
export type ResetPasswordSchemaType = z.infer<typeof resetPasswordSchema>;
````

## File: frontend/tests/smoke.test.tsx
````typescript
import React from "react";
import { render, screen } from "@testing-library/react";
import HomePage from "@/app/page";

describe("Next.js Storefront Root Application Smoke Test Suite", () => {
  it("should successfully mount and render the main home page component layout without throwing errors", () => {
    const { container } = render(<HomePage />);

    // Assert structural visibility matches layout expectations
    const headingElement = screen.getByRole("heading", {
      level: 1,
      name: /e-commerce storefront/i,
    });
    expect(headingElement).toBeInTheDocument();

    const actionButton = screen.getByRole("button", { name: /browse products/i });
    expect(actionButton).toBeInTheDocument();

    // Verify container generated real HTML rendering paths
    expect(container.firstChild).toBeInTheDocument();
  });
});
````

## File: frontend/types/address.ts
````typescript
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
````

## File: frontend/tsconfig.json
````json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": [
        "./*"
      ]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}
````

## File: backend/app/api/routes/categories.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryOut, CategoryCreate, CategoryUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
async def get_categories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category))
    return result.scalars().all()


@router.get("/categories/{category_id}", response_model=CategoryOut)
async def get_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/categories", response_model=CategoryOut, status_code=201)
async def create_category(
    payload: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Category name already exists")

    new_category = Category(
        name=payload.name,
        description=payload.description,
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category


@router.put("/categories/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    await db.commit()
    await db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    await db.delete(category)
    await db.commit()
    return None
````

## File: backend/app/api/routes/customer_profiles.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.address import Address
from app.schemas.customer_profile import CustomerProfileOut, CustomerProfileUpdate
from app.schemas.address import AddressCreate, AddressUpdate, AddressOut
from app.core.auth import get_current_user

router = APIRouter(prefix="/customer/profile", tags=["Customer Profile"])


@router.get("/me", response_model=CustomerProfileOut)
async def get_customer_profile(current_user: User = Depends(get_current_user)):
    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.put("/me", response_model=CustomerProfileOut)
async def update_customer_profile(
    payload: CustomerProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    await db.commit()
    await db.refresh(current_user)

    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.get("/addresses", response_model=list[AddressOut])
async def list_addresses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
    result = await db.execute(stmt)
    return list(result.scalars().all())


@router.post("/addresses", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    payload: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if payload.is_default:
        stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
        result = await db.execute(stmt)
        for existing in result.scalars().all():
            existing.is_default = False

    address = Address(customer_id=current_user.customer_profile.id, **payload.dict())
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


@router.put("/addresses/{address_id}", response_model=AddressOut)
async def update_address(
    address_id: int,
    payload: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = payload.dict(exclude_unset=True)

    if update_data.get("is_default"):
        stmt = select(Address).where(
            Address.customer_id == current_user.customer_profile.id,
            Address.id != address_id,
        )
        result = await db.execute(stmt)
        for other in result.scalars().all():
            other.is_default = False

    for field, value in update_data.items():
        setattr(address, field, value)

    await db.commit()
    await db.refresh(address)
    return address


@router.delete("/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    await db.delete(address)
    await db.commit()
    return None
````

## File: backend/app/api/routes/payments.py
````python
import stripe
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.auth import get_current_user
from app.core.config import settings
from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User

router = APIRouter()

stripe.api_key = settings.STRIPE_SECRET_KEY  # <-- FLAG: pulled from Settings, confirm STRIPE_SECRET_KEY is set in .env

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _validate_cart_stock(db: AsyncSession, cart: Cart) -> float:
    """Validates stock for every line item, returns computed total."""
    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )
        total += float(variant.price) * item.quantity
    return total


@router.post("/payments/create-intent")
async def create_payment_intent(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = await _validate_cart_stock(db, cart)
    if total <= 0:
        raise HTTPException(status_code=400, detail="Invalid cart total")

    amount_in_cents = int(round(total * 100))

    intent = stripe.PaymentIntent.create(
        amount=amount_in_cents,
        currency="usd",  # <-- FLAG: confirm currency; hardcoded for now
        metadata={
            "cart_id": str(cart.id),
            "customer_id": str(profile.id),
        },
        automatic_payment_methods={"enabled": True},
    )

    return {"client_secret": intent.client_secret}

async def _create_order_from_cart(db: AsyncSession, cart_id: int, customer_id: int) -> None:
    result = await db.execute(
        select(Cart)
        .options(_CART_ITEM_LOAD)
        .where(Cart.id == cart_id, Cart.customer_id == customer_id)
        .with_for_update()
        .execution_options(populate_existing=True)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        return

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.id == customer_id))
    profile = result.scalar_one_or_none()
    if not profile:
        return

    new_order = Order(
        customer_id=profile.id,
        order_status="paid",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant:
            continue

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in list(cart.items):
        cart.items.remove(item)
        await db.delete(item)

    await db.commit()


@router.post("/payments/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET  # <-- FLAG: pulled from Settings, confirm STRIPE_WEBHOOK_SECRET is set in .env
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        metadata = intent.get("metadata", {})
        cart_id = metadata.get("cart_id")
        customer_id = metadata.get("customer_id")

        if cart_id and customer_id:
            await _create_order_from_cart(db, int(cart_id), int(customer_id))

    return {"status": "success"}
````

## File: backend/app/api/routes/users.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.core.security import hash_password
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER
from app.core.auth import get_current_user_optional

router = APIRouter()

CUSTOMER_ROLE_ID = 4


@router.get("/users", response_model=list[UserOut])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(User).options(selectinload(User.role)))
    return result.scalars().all()


@router.post("/users", response_model=UserOut, status_code=201)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional)
):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    if current_user is not None and current_user.role_id == 1:
        final_role_id = payload.role_id
    else:
        final_role_id = CUSTOMER_ROLE_ID

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        avatar_url=payload.avatar_url,
        role_id=final_role_id,
        is_active=payload.is_active,
    )

    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == new_user.id)
    )
    result = await db.execute(stmt)
    created_user = result.scalar_one()

    return created_user


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    block_manager_on_admin_target(current_user, user.role_id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == user_id)
    )
    result = await db.execute(stmt)
    updated_user = result.scalar_one()

    return updated_user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return None
````

## File: backend/app/core/config.py
````python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SMTP_HOST: str = "sandbox.smtp.mailtrap.io"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = "PLACEHOLDER_USERNAME"
    SMTP_PASSWORD: str = "PLACEHOLDER_PASSWORD"
    FROM_EMAIL: str = "no-reply@yourapp.com"
    FRONTEND_URL: str = "https://yourapp.com"

    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    TEST_MODE: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()
````

## File: backend/app/database/base.py
````python
from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str


    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
````

## File: backend/app/models/cart_item.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int] = mapped_column(ForeignKey("product_variants.id"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    cart: Mapped["Cart"] = relationship(back_populates="items")
    product_variant: Mapped["ProductVariant"] = relationship()
````

## File: backend/app/seed.py
````python
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.session import AsyncSessionLocal
from app.models.role import Role
from app.models.user import User
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.core.security import hash_password

RESOURCES = [
    "users", "roles", "permissions",
    "categories", "products", "product_categories",
    "product_variants", "orders", "order_items"
]
ACTIONS = ["create", "read", "update", "delete"]

# Updated to include our storefront target
ROLES = ["admin", "manager", "staff", "customer"]

ROLE_ACTIONS = {
    "admin": ["create", "read", "update", "delete"],
    "manager": ["create", "read", "update"],
    "staff": ["read"],
    "customer": ["read"], # Storefront customers can only view catalog items natively
}

async def get_or_create_role(db: AsyncSession, name: str, description: str) -> Role:
    result = await db.execute(select(Role).filter(Role.name == name))
    role = result.scalar_one_or_none()
    if not role:
        role = Role(id=uuid.uuid4(), name=name, description=description)
        db.add(role)
        await db.commit()
        await db.refresh(role)
        print(f"Created role: {role.name} (id={role.id})")
    else:
        print(f"Role already exists: {role.name} (id={role.id})")
    return role

async def get_or_create_permission(db: AsyncSession, name: str, description: str) -> Permission:
    result = await db.execute(select(Permission).filter(Permission.name == name))
    perm = result.scalar_one_or_none()
    if not perm:
        perm = Permission(id=uuid.uuid4(), name=name, description=description)
        db.add(perm)
        await db.commit()
        await db.refresh(perm)
    return perm

async def link_role_permission(db: AsyncSession, role_id: uuid.UUID, permission_id: uuid.UUID) -> None:
    result = await db.execute(
        select(RolePermission).filter(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id
        )
    )
    exists = result.scalar_one_or_none()
    if not exists:
        db.add(RolePermission(id=uuid.uuid4(), role_id=role_id, permission_id=permission_id))

async def seed_database(db: AsyncSession) -> None:
    """
    Idempotent asynchronous database seeder managing RBAC systems
    and the Customer tier.
    """
    print("Checking database for seed records...")

    # 1. Create all roles asynchronously
    role_objs = {}
    for role_name in ROLES:
        role_objs[role_name] = await get_or_create_role(
            db, role_name, f"{role_name.capitalize()} role"
        )

    # 2. Create all permissions (resource:action)
    permission_objs = {}
    for resource in RESOURCES:
        for action in ACTIONS:
            perm_name = f"{resource}:{action}"
            permission_objs[perm_name] = await get_or_create_permission(
                db, perm_name, f"Can {action} {resource}"
            )
    await db.commit()
    print(f"Ensured {len(permission_objs)} permissions exist")

    # 3. Link roles to permissions
    for role_name, allowed_actions in ROLE_ACTIONS.items():
        role = role_objs[role_name]
        for resource in RESOURCES:
            for action in allowed_actions:
                perm_name = f"{resource}:{action}"
                await link_role_permission(db, role.id, permission_objs[perm_name].id)
    await db.commit()
    print("Linked role-permission mappings")

    # 4. Create admin user
    admin_email = "admin@rbac.com"
    user_query = await db.execute(select(User).filter(User.email == admin_email))
    admin_user = user_query.scalar_one_or_none()

    if not admin_user:
        admin_user = User(
            id=uuid.uuid4(),
            full_name="Admin",
            email=admin_email,
            hashed_password=hash_password("Admin123!"),
            is_active=True,
            role_id=role_objs["admin"].id
        )
        db.add(admin_user)
        await db.commit()
        await db.refresh(admin_user)
        print(f"Created user: {admin_user.email} (id={admin_user.id})")
    else:
        print(f"User already exists: {admin_user.email} (id={admin_user.id})")

    print("Seeding checks complete!")

async def run_seed_cli() -> None:
    """Entry point for manual execution via terminal"""
    async with AsyncSessionLocal() as session:
        await seed_database(session)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_seed_cli())
````

## File: backend/requirements.txt
````
alembic==1.18.5
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.1
bcrypt==5.0.0
cffi==2.0.0
click==8.4.2
colorama==0.4.6
cryptography==49.0.0
dnspython==2.8.0
ecdsa==0.19.2
email-validator==2.3.0
fastapi==0.139.0
greenlet==3.5.3
h11==0.16.0
idna==3.18
Mako==1.3.12
MarkupSafe==3.0.3
psycopg==3.3.4
psycopg-binary==3.3.4
pyasn1==0.6.3
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.14.2
pydantic_core==2.46.4
python-dotenv==1.2.2
python-jose==3.5.0
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.51
starlette==1.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
tzdata==2026.2
uvicorn==0.49.0
stripe
````

## File: frontend/lib/api/auth.ts
````typescript
import { apiClient, ApiError } from "./client";
import { AuthTokenResponse } from "@/types/api";
import {
  LoginSchemaType,
  RegisterSchemaType,
  ResetPasswordSchemaType,
  ForgotPasswordSchemaType,
} from "@/lib/validation/auth";

const FALLBACK_MESSAGES = {
  login: "We couldn't sign you in. Please check your credentials and try again.",
  register: "We couldn't create your account. Please try again.",
  refresh: "Your session has expired. Please log in again.",
  logout: "We couldn't log you out. Please try again.",
  forgotPassword: "We couldn't send the password reset email. Please try again.",
  resetPassword: "We couldn't reset your password. Please try again.",
  verifyEmail: "We couldn't verify your email. Please try again.",
  resendVerification: "We couldn't resend the verification email. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

// POST /customer/auth/register — returns id/name/email/emailVerified/message, NOT a token
export async function register(
  userData: RegisterSchemaType,
  signal?: AbortSignal
): Promise<{ id: number; name: string; email: string; emailVerified: boolean; message: string }> {
  try {
    return await apiClient.post("/customer/auth/register", userData, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.register);
  }
}

// POST /customer/auth/login
export async function login(
  credentials: LoginSchemaType,
  signal?: AbortSignal
): Promise<AuthTokenResponse> {
  try {
    return await apiClient.post<AuthTokenResponse>("/customer/auth/login", credentials, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.login);
  }
}

// POST /customer/auth/refresh
export async function refreshToken(
  refreshToken: string,
  signal?: AbortSignal
): Promise<AuthTokenResponse> {
  try {
    return await apiClient.post<AuthTokenResponse>(
      "/customer/auth/refresh",
      { refresh_token: refreshToken },
      { signal, skipAuthRetry: true }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

// POST /customer/auth/logout
export async function logout(
  refreshToken: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post(
      "/customer/auth/logout",
      { refresh_token: refreshToken },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.logout);
  }
}

// POST /customer/auth/verify-email
export async function verifyEmail(
  token: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/verify-email", { token }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.verifyEmail);
  }
}

// POST /customer/auth/resend-verification
export async function resendVerification(
  email: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/resend-verification", { email }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resendVerification);
  }
}

// POST /customer/auth/forgot-password
export async function forgotPassword(
  data: ForgotPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/forgot-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.forgotPassword);
  }
}

// POST /customer/auth/reset-password
export async function resetPassword(
  data: ResetPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/reset-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resetPassword);
  }
}
````

## File: frontend/lib/api/users.ts
````typescript
import { apiClient, ApiError } from "./client";
import { CustomerProfile, CustomerProfileUpdate } from "@/types/user";
import { Address, AddressCreate, AddressUpdate } from "@/types/address";

const BASE = "/customer/profile";

const FALLBACK_MESSAGES = {
  getProfile: "We couldn't load your profile. Please try again.",
  updateProfile: "We couldn't update your profile. Please try again.",
  listAddresses: "We couldn't load your addresses. Please try again.",
  createAddress: "We couldn't add that address. Please try again.",
  updateAddress: "We couldn't update that address. Please try again.",
  deleteAddress: "We couldn't delete that address. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

// GET /customer/profile/me
export async function getProfile(signal?: AbortSignal): Promise<CustomerProfile> {
  try {
    return await apiClient.get<CustomerProfile>(`${BASE}/me`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProfile);
  }
}

// PUT /customer/profile/me
export async function updateProfile(
  data: CustomerProfileUpdate,
  signal?: AbortSignal
): Promise<CustomerProfile> {
  try {
    return await apiClient.put<CustomerProfile>(`${BASE}/me`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateProfile);
  }
}

// GET /customer/profile/addresses
export async function listAddresses(signal?: AbortSignal): Promise<Address[]> {
  try {
    return await apiClient.get<Address[]>(`${BASE}/addresses`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.listAddresses);
  }
}

// POST /customer/profile/addresses
export async function createAddress(data: AddressCreate, signal?: AbortSignal): Promise<Address> {
  try {
    return await apiClient.post<Address>(`${BASE}/addresses`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createAddress);
  }
}

// PUT /customer/profile/addresses/{addressId}
export async function updateAddress(
  addressId: number,
  data: AddressUpdate,
  signal?: AbortSignal
): Promise<Address> {
  try {
    return await apiClient.put<Address>(`${BASE}/addresses/${addressId}`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateAddress);
  }
}

// DELETE /customer/profile/addresses/{addressId} — 204 No Content
export async function deleteAddress(addressId: number, signal?: AbortSignal): Promise<void> {
  try {
    await apiClient.delete(`${BASE}/addresses/${addressId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.deleteAddress);
  }
}
````

## File: frontend/types/api.ts
````typescript
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
````

## File: frontend/types/order.ts
````typescript
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
````

## File: frontend/types/product.ts
````typescript
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
````

## File: frontend/types/user.ts
````typescript
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
````

## File: frontend/package.json
````json
{
  "name": "ecommerce-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  },
  "dependencies": {
    "next": "^16.2.12",
    "postcss": "^8.5.23",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "sharp": "^0.35.3",
    "zod": "^3.23.8",
    "zustand": "^5.0.14"
  },
  "devDependencies": {
    "@playwright/test": "^1.61.1",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.4.2",
    "@testing-library/react": "^16.0.0",
    "@types/jest": "^29.5.12",
    "@types/node": "^20.11.24",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "brace-expansion": "^5.0.8",
    "eslint": "^10.8.0",
    "eslint-config-next": "^16.2.12",
    "jest": "^30.0.0",
    "jest-environment-jsdom": "^30.0.0",
    "ts-jest": "^29.2.0",
    "ts-node": "^10.9.2",
    "typescript": "^5.3.3"
  },
  "overrides": {
    "brace-expansion": "^5.0.8",
    "minimatch": "^10.2.5",
    "postcss": "^8.5.23",
    "sharp": "^0.35.3"
  }
}
````

## File: backend/app/api/routes/auth.py
````python
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.schemas.auth import LoginRequest, Token, ForgotPasswordRequest, ResetPasswordRequest
from app.core.jwt import create_access_token
from app.core.security import verify_password, hash_password
from app.core.auth import get_current_user
from app.core.email import send_password_reset_email
from pydantic import BaseModel

router = APIRouter()

RESET_TOKEN_EXPIRE_HOURS = 1


class MsgResponse(BaseModel):
    message: str


@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role_id": user.role_id,
        }
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .where(RolePermission.role_id == current_user.role_id)
    )
    result = await db.execute(stmt)
    permissions = list(result.scalars().all())

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role_id": current_user.role_id,
        "role": {
            "id": current_user.role.id,
            "name": current_user.role.name,
            "description": current_user.role.description,
        } if current_user.role else None,
        "is_active": current_user.is_active,
        "created_at": current_user.created_at,
        "updated_at": current_user.updated_at,
        "permissions": permissions,
    }


@router.post("/forgot-password", response_model=MsgResponse)
async def forgot_password(payload: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(
        message="If that email exists, a password reset link has been sent."
    )

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(
        hours=RESET_TOKEN_EXPIRE_HOURS
    )
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def reset_password(payload: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if (
        not user.password_reset_expires_at
        or user.password_reset_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="User account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(
        message="Password has been reset successfully. Please log in with your new password."
    )
````

## File: backend/app/api/routes/order_items.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.models.product_variant import ProductVariant
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemOut, OrderItemCreate, OrderItemUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()

# #TODO: final check if completed is the exact status indicator.
LOCKED_STATUS = "completed"


def _assert_order_editable(order: Order) -> None:
    if order.order_status == LOCKED_STATUS:
        raise HTTPException(
            status_code=400,
            detail=f"Order is '{LOCKED_STATUS}' and can no longer be modified",
        )

async def recalculate_total(order_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    total = sum(item.quantity * float(item.price_at_purchase) for item in result.scalars().all())

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        return

    order.total_amount = total
    await db.commit()


@router.get("/orders/{order_id}/items", response_model=list[OrderItemOut])
async def get_order_items(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    return result.scalars().all()


@router.post("/orders/{order_id}/items", response_model=OrderItemOut, status_code=201)
async def add_order_item(
    order_id: int,
    payload: OrderItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == payload.product_variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    if variant.stock_quantity < payload.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
        )

    new_item = OrderItem(
        order_id=order_id,
        product_variant_id=payload.product_variant_id,
        quantity=payload.quantity,
        price_at_purchase=payload.price_at_purchase,
    )
    variant.stock_quantity -= payload.quantity
    db.add(new_item)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid product_variant_id")

    await db.refresh(new_item)
    await recalculate_total(order_id, db)
    await db.refresh(new_item)
    return new_item


@router.put("/order-items/{item_id}", response_model=OrderItemOut)
async def update_order_item(
    item_id: int,
    payload: OrderItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    update_data = payload.model_dump(exclude_unset=True)

    if "quantity" in update_data:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if not variant:
            raise HTTPException(status_code=404, detail="Product variant not found")

        old_quantity = item.quantity
        new_quantity = update_data["quantity"]
        diff = new_quantity - old_quantity

        if diff > 0 and variant.stock_quantity < diff:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
            )

        variant.stock_quantity -= diff

    for field, value in update_data.items():
        setattr(item, field, value)

    await db.commit()
    await db.refresh(item)
    await recalculate_total(item.order_id, db)
    await db.refresh(item)
    return item


@router.delete("/order-items/{item_id}", status_code=204)
async def delete_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    if item.product_variant_id is not None:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if variant:
            variant.stock_quantity += item.quantity

    order_id = item.order_id
    await db.delete(item)
    await db.commit()

    await recalculate_total(order_id, db)
    return None
````

## File: backend/app/api/routes/orders.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.schemas.order import OrderOut, OrderCreate, OrderUpdate, OrderStatusUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/orders", response_model=list[OrderOut])
async def get_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order))
    return result.scalars().all()


@router.get("/orders/{order_id}", response_model=OrderOut)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/orders", response_model=OrderOut, status_code=201)
async def create_order(
    payload: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    new_order = Order(
        customer_id=payload.customer_id,
        guest_name=payload.guest_name,
        guest_email=payload.guest_email,
        guest_phone=payload.guest_phone,
        order_status=payload.order_status,
        total_amount=0,
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order


@router.put("/orders/{order_id}", response_model=OrderOut)
async def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(order, field, value)

    await db.commit()
    await db.refresh(order)
    return order


@router.patch("/orders/{order_id}/status", response_model=OrderOut)
async def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = payload.status
    await db.commit()
    await db.refresh(order)
    return order


@router.delete("/orders/{order_id}", status_code=204)
async def delete_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    await db.delete(order)
    await db.commit()
    return None
````

## File: backend/app/models/cart.py
````python
import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=True, unique=True
    )
    guest_token: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True, unique=True, index=True)
    coupon_id: Mapped[int | None] = mapped_column(ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    expires_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    items: Mapped[list["CartItem"]] = relationship(back_populates="cart", cascade="all, delete-orphan")
    coupon: Mapped["Coupon"] = relationship(back_populates="carts")
    customer: Mapped["CustomerProfile"] = relationship(back_populates="cart")
````

## File: backend/app/schemas/cart.py
````python
from pydantic import BaseModel, Field
import uuid


class CartItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)


class CartItemOut(BaseModel):
    id: int
    product_variant_id: int
    quantity: int
    unit_price: float
    subtotal: float

    class Config:
        from_attributes = True


class CartOut(BaseModel):
    id: int
    customer_id: int | None
    guest_token: uuid.UUID | None
    coupon_id: int | None
    items: list[CartItemOut]
    total: float

    class Config:
        from_attributes = True


class CartMergeRequest(BaseModel):
    guest_token: str


class ApplyCouponRequest(BaseModel):
    code: str
````

## File: backend/app/schemas/order.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.order_item import OrderItemOut


class OrderOut(BaseModel):
    id: int
    customer_id: int | None = None
    status: str | None = None
    guest_name: str | None = None
    guest_email: str | None = None
    guest_phone: str | None = None
    shipping_address_id: int | None = None
    billing_address_id: int | None = None
    coupon_id: int | None = None
    order_status: str
    subtotal: float
    discount_amount: float
    shipping_amount: float
    tax_amount: float
    total_amount: float
    notes: str | None = None
    created_at: datetime
    placed_at: datetime | None = None
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="before")
    @classmethod
    def populate_status_compat(cls, data):
        if isinstance(data, dict):
            if data.get("status") is None and data.get("order_status") is not None:
                data = dict(data)
                data["status"] = data["order_status"]
        return data


class OrderCreate(BaseModel):
    customer_id: int | None = None
    guest_name: str | None = Field(default=None, max_length=100)
    guest_email: str | None = Field(default=None, max_length=255)
    guest_phone: str | None = Field(default=None, max_length=20)
    order_status: str = Field(default="open", max_length=20)


class OrderUpdate(BaseModel):
    order_status: str | None = Field(default=None, max_length=20)
    notes: str | None = None


class OrderStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
````

## File: .gitignore
````
# ---------- Node / Next.js (frontend) ----------
node_modules/
.next/
out/
build/
dist/
.pnp/
.pnp.js

# env files
.env
.env.local
.env.*.local
.env.production
.env.development
!.env.example

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# testing
coverage/
playwright-report/
test-results/

# misc
.DS_Store
*.pem
next-env.d.ts
.vercel

# ---------- Python / FastAPI (backend) ----------
# Explicitly target nested __pycache__ and bytecode
**/__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Explicitly target backend virtual environment paths
backend/venv/
backend/env/
backend/.venv/

# alembic (keep versions, ignore local db files)
*.sqlite3
*.db

# env files (backend)
backend/.env
backend/.env.production
backend/.env.development
backend/.env.test
backend/repomix-output.md

# ---------- Editors / OS ----------
.vscode/
.idea/
*.swp
Thumbs.db
.DS_Store

# ---------- Docker ----------
*.log
docker-compose.override.yml

#-------Repomix -------------
repomix-output.xml
````

## File: backend/app/api/routes/cart.py
````python
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartOut,
    CartMergeRequest,
    ApplyCouponRequest,
)
from app.core.auth import get_current_user_optional

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


def _compute_total(cart: Cart) -> float:
    return sum(float(item.product_variant.price) * item.quantity for item in cart.items)


def _serialize_cart(cart: Cart) -> dict:
    return {
        "id": cart.id,
        "customer_id": cart.customer_id,
        "guest_token": cart.guest_token,
        "coupon_id": cart.coupon_id,
        "items": [
            {
                "id": item.id,
                "product_variant_id": item.product_variant_id,
                "quantity": item.quantity,
                "unit_price": float(item.product_variant.price),
                "subtotal": float(item.product_variant.price) * item.quantity,
            }
            for item in cart.items
        ],
        "total": _compute_total(cart),
    }


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_or_create_cart(
    db: AsyncSession,
    current_user: User | None,
    guest_token: str | None,
) -> Cart:
    if current_user:
        profile = await _get_or_create_customer_profile(db, current_user)

        result = await db.execute(
            select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(customer_id=profile.id)
            db.add(cart)
            await db.commit()
            cart = await _reload_cart(db, cart.id)
        return cart

    if not guest_token:
        raise HTTPException(status_code=400, detail="Guest token required for guest cart")

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.guest_token == guest_token)
    )
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(guest_token=guest_token)
        db.add(cart)
        await db.commit()
        cart = await _reload_cart(db, cart.id)
    return cart


async def _reload_cart(db: AsyncSession, cart_id: int) -> Cart:
    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.id == cart_id)
    )
    return result.scalar_one()


@router.get("/cart", response_model=CartOut)
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    return _serialize_cart(cart)


@router.post("/cart/items", response_model=CartOut, status_code=201)
async def add_cart_item(
    payload: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(
        select(ProductVariant).where(ProductVariant.id == payload.product_variant_id)
    )
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.cart_id == cart.id,
            CartItem.product_variant_id == payload.product_variant_id,
        )
    )
    existing_item = result.scalar_one_or_none()

    if existing_item:
        existing_item.quantity += payload.quantity
    else:
        new_item = CartItem(
            cart_id=cart.id,
            product_variant_id=payload.product_variant_id,
            quantity=payload.quantity,
        )
        db.add(new_item)

    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.put("/cart/items/{item_id}", response_model=CartOut)
async def update_cart_item(
    item_id: int,
    payload: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = payload.quantity
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/items/{item_id}", response_model=CartOut)
async def delete_cart_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    await db.delete(item)
    await db.commit()

    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.post("/cart/merge", response_model=CartOut)
async def merge_cart(
    payload: CartMergeRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user_optional),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Login required to merge cart")

    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Cart).where(Cart.guest_token == payload.guest_token))
    guest_cart = result.scalar_one_or_none()
    if not guest_cart:
        raise HTTPException(status_code=404, detail="Guest cart not found")

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    user_cart = result.scalar_one_or_none()
    if not user_cart:
        guest_cart.customer_id = profile.id
        guest_cart.guest_token = None
        await db.commit()
        cart = await _reload_cart(db, guest_cart.id)
        return _serialize_cart(cart)

    result = await db.execute(select(CartItem).where(CartItem.cart_id == guest_cart.id))
    guest_items = result.scalars().all()
    for guest_item in guest_items:
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == user_cart.id,
                CartItem.product_variant_id == guest_item.product_variant_id,
            )
        )
        existing_item = result.scalar_one_or_none()
        if existing_item:
            existing_item.quantity += guest_item.quantity
        else:
            db.add(CartItem(
                cart_id=user_cart.id,
                product_variant_id=guest_item.product_variant_id,
                quantity=guest_item.quantity,
            ))

    await db.delete(guest_cart)
    await db.commit()
    user_cart = await _reload_cart(db, user_cart.id)
    return _serialize_cart(user_cart)


@router.post("/cart/apply-coupon", response_model=CartOut)
async def apply_coupon(
    payload: ApplyCouponRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(select(Coupon).where(Coupon.code == payload.code))
    coupon = result.scalar_one_or_none()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    if not coupon.is_active:
        raise HTTPException(status_code=400, detail="Coupon is not active")

    now = datetime.now(timezone.utc)
    if now < coupon.start_date or now > coupon.end_date:
        raise HTTPException(status_code=400, detail="Coupon is not valid at this time")

    if coupon.usage_limit is not None and coupon.usage_count >= coupon.usage_limit:
        raise HTTPException(status_code=400, detail="Coupon usage limit reached")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    cart_total = _compute_total(cart)
    min_order = coupon.minimum_order_amount or 0
    if cart_total < float(min_order):
        raise HTTPException(
            status_code=400,
            detail=f"Order must be at least {min_order} to use this coupon",
        )

    cart.coupon_id = coupon.id
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/coupon", response_model=CartOut)
async def remove_coupon(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    cart.coupon_id = None
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)
````

## File: backend/app/core/auth.py
````python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.core.jwt import verify_access_token

security = HTTPBearer()
security_optional = HTTPBearer(auto_error=False)


async def _get_current_user_by_token(token: str, db: AsyncSession) -> User:
    payload = verify_access_token(token)

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    stmt = (
        select(User)
        .options(selectinload(User.role), selectinload(User.customer_profile))
        .where(User.id == int(user_id))
    )
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    return await _get_current_user_by_token(credentials.credentials, db)


async def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials | None = Depends(security_optional),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    if not credentials:
        return None

    try:
        return await _get_current_user_by_token(credentials.credentials, db)
    except HTTPException:
        return None
````

## File: backend/app/models/order.py
````python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="SET NULL"), nullable=True
    )
    guest_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    guest_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    guest_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    shipping_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    billing_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    coupon_id: Mapped[int | None] = mapped_column(
        ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True
    )

    order_status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")

    subtotal: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    discount_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    shipping_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    placed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    def __init__(self, **kwargs):
        if "status" in kwargs and "order_status" not in kwargs:
            kwargs["order_status"] = kwargs.pop("status")
        if "customer_name" in kwargs:
            self._customer_name = kwargs.pop("customer_name")
        super().__init__(**kwargs)

    @property
    def status(self) -> str:
        return self.order_status

    @status.setter
    def status(self, value: str) -> None:
        self.order_status = value

    @property
    def customer_name(self) -> str | None:
        return getattr(self, "_customer_name", None)

    @customer_name.setter
    def customer_name(self, value: str | None) -> None:
        self._customer_name = value

    # Relationships
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    customer: Mapped["CustomerProfile"] = relationship()
````

## File: backend/app/models/user.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    phone_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    password_reset_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    password_reset_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    email_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    email_verification_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    email_verification_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    refresh_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    refresh_token_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    customer_profile: Mapped["CustomerProfile"] = relationship(
        back_populates="user", uselist=False
    )
````

## File: backend/tests/conftest.py
````python
import os
import sys
import asyncio
from datetime import datetime, timedelta, timezone

os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:admin@localhost:5432/ecommerce_test")
os.environ.setdefault("SECRET_KEY", "test-secret-key-do-not-use-in-prod")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_dummy")
os.environ.setdefault("STRIPE_WEBHOOK_SECRET", "whsec_dummy")
os.environ.setdefault("TEST_MODE", "false")

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.cart import Cart
from app.models.cart_item import CartItem

from app.database.base import Base
from app.database.session import get_db
from app.core.config import settings
from app.core.jwt import create_access_token
from app.core.security import hash_password
from app.models.user import User
from app.models.role import Role
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem

import app.models  # noqa: F401  registers all model metadata
from app.main import app as fastapi_app

STAFF_ROLE_ID = 3
CUSTOMER_ROLE_ID = 4

test_engine = create_async_engine(settings.DATABASE_URL, future=True, poolclass=NullPool)
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


@pytest_asyncio.fixture(scope="session", autouse=True, loop_scope="session")
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestSessionLocal() as session:
        result = await session.execute(select(Role).where(Role.id.in_([STAFF_ROLE_ID, CUSTOMER_ROLE_ID])))
        existing_role_ids = {role.id for role in result.scalars()}
        if STAFF_ROLE_ID not in existing_role_ids:
            session.add(Role(id=STAFF_ROLE_ID, name="staff", description="Staff role"))
        if CUSTOMER_ROLE_ID not in existing_role_ids:
            session.add(Role(id=CUSTOMER_ROLE_ID, name="customer", description="Customer role"))
        if STAFF_ROLE_ID not in existing_role_ids or CUSTOMER_ROLE_ID not in existing_role_ids:
            await session.commit()
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest_asyncio.fixture
async def db():
    async with test_engine.connect() as connection:
        await connection.begin()
        session = AsyncSession(
            bind=connection,
            expire_on_commit=False,
            join_transaction_mode="create_savepoint",
        )
        try:
            yield session
        finally:
            await session.close()
            await connection.rollback()


@pytest_asyncio.fixture
async def client(db):
    async def override_get_db():
        yield db

    fastapi_app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    fastapi_app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def make_customer(db):
    async def _make_customer(email="customer@example.com", password="Password123!", verified=True, active=True):
        user = User(
            name="Test Customer",
            email=email,
            password=hash_password(password),
            role_id=CUSTOMER_ROLE_ID,
            is_active=active,
            email_verified=verified,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()

        return user, password

    return _make_customer


@pytest_asyncio.fixture
async def auth_headers():
    def _auth_headers(user):
        token = create_access_token({"sub": str(user.id), "email": user.email, "role_id": user.role_id})
        return {"Authorization": f"Bearer {token}"}

    return _auth_headers


@pytest.fixture(autouse=True)
def mock_emails(monkeypatch):
    sent = {"verification": [], "reset": []}

    def fake_verification(to, token):
        sent["verification"].append((to, token))

    def fake_reset(to, token):
        sent["reset"].append((to, token))

    monkeypatch.setattr("app.api.routes.customer_auth.send_verification_email", fake_verification)
    monkeypatch.setattr("app.api.routes.customer_auth.send_password_reset_email", fake_reset)

    return sent


@pytest_asyncio.fixture
async def make_product_variant(db):
    counter = {"n": 0}

    async def _make_product_variant(price=19.99, stock_quantity=10, is_active=True):
        counter["n"] += 1
        n = counter["n"]

        product = Product(
            name=f"Test Product {n}",
            description="Seeded for checkout tests",
            price=price,
            is_active=True,
        )
        db.add(product)
        await db.flush()

        variant = ProductVariant(
            product_id=product.id,
            sku=f"TEST-SKU-{n}",
            price=price,
            stock_quantity=stock_quantity,
            is_active=is_active,
        )
        db.add(variant)
        await db.commit()
        await db.refresh(variant)

        return variant

    return _make_product_variant


@pytest_asyncio.fixture
async def make_cart_with_item(db):
    async def _make_cart_with_item(customer_profile_id, variant, quantity=1):
        cart = Cart(customer_id=customer_profile_id)
        db.add(cart)
        await db.flush()

        item = CartItem(cart_id=cart.id, product_variant_id=variant.id, quantity=quantity)
        db.add(item)
        await db.commit()
        await db.refresh(cart)

        return cart

    return _make_cart_with_item


@pytest_asyncio.fixture
async def make_order_item(db, make_product_variant):
    async def _make_order_item(customer_profile_id, variant=None, quantity=1):
        if variant is None:
            variant = await make_product_variant()

        order = Order(
            customer_id=customer_profile_id,
            order_status="completed",
            total_amount=float(variant.price) * quantity,
        )
        db.add(order)
        await db.flush()

        order_item = OrderItem(
            order_id=order.id,
            product_variant_id=variant.id,
            quantity=quantity,
            price_at_purchase=float(variant.price),
        )
        db.add(order_item)
        await db.commit()
        await db.refresh(order_item)

        return order_item, variant.product_id

    return _make_order_item


@pytest_asyncio.fixture
async def make_staff(db):
    async def _make_staff(email="staff@example.com", password="Password123!"):
        user = User(
            name="Test Staff",
            email=email,
            password=hash_password(password),
            role_id=STAFF_ROLE_ID,
            is_active=True,
            email_verified=True,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user, password

    return _make_staff
````

## File: backend/app/models/__init__.py
````python
from .user import User
from .role import Role
from .permission import Permission
from .role_permission import RolePermission
from .product import Product
from .product_category import ProductCategory
from .category import Category
from .product_variant import ProductVariant
from .order import Order
from .order_item import OrderItem
from .cart import Cart
from .cart_item import CartItem
from .coupon import Coupon
from .customer_profile import CustomerProfile
from .address import Address
from .review import Review
from .wishlist import Wishlist
from app.models.payment import Payment
from .return_request import ReturnRequest
````

## File: backend/app/main.py
````python
from fastapi import FastAPI
from sqlalchemy import text
from app.seed import seed_database
import app.models
from app.database.session import engine, AsyncSessionLocal
from app.core.config import settings
from app.core.test_seed import ensure_bogus_data
from app.api.routes.users import router as users_router
from app.api.routes.roles import router as roles_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.role_permissions import router as role_permissions_router
from app.api.routes.categories import router as categories_router
from app.api.routes.products import router as products_router
from app.api.routes.product_categories import router as product_categories_router
from app.api.routes.product_variants import router as product_variants_router
from app.api.routes.orders import router as orders_router
from app.api.routes.order_items import router as order_items_router
from app.api.routes.auth import router as auth_router
from app.api.routes.customer_profiles import router as customer_router
from app.api.routes.cart import router as cart_router
from app.api.routes.reviews import router as reviews_router
from app.api.routes.payments import router as payments_router
from app.api.routes.customer_auth import router as customer_auth_router
from app.api.routes.checkout import router as checkout_router
from app.api.routes.wishlist import router as wishlist_router
from app.api.routes.customer_order import router as customer_order_router

app = FastAPI()

ROUTERS = [
    (users_router, "Users"),
    (auth_router, "Auth-Admin"),
    (roles_router, "Roles"),
    (permissions_router, "Permissions"),
    (role_permissions_router, "Role Permissions"),
    (products_router, "Products"),
    (categories_router, "Categories"),
    (product_categories_router, "Product Categories"),
    (product_variants_router, "Product Variants"),
    (orders_router, "Orders-Admin"),
    (order_items_router, "Order Items"),
    (customer_auth_router, "Customer Auth"),
    (customer_router, "Customer Profile"),
    (cart_router, "Cart"),
    (reviews_router, "Reviews"),
    (payments_router, "Payments"),
    (checkout_router, "Checkout"),
    (wishlist_router, "Wishlist"),
    (customer_order_router, "Customer Orders"),
]

for router, tag in ROUTERS:
    app.include_router(router, tags=[tag])


@app.on_event("startup")
async def on_startup():
    if settings.TEST_MODE:
        async with AsyncSessionLocal() as db:
            await ensure_bogus_data(db)
        print("TEST_MODE is ON — bogus product/variant/coupon seeded (id 999001 / code TESTCODE10)")


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)
````
