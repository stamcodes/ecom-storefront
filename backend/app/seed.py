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