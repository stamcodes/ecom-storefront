# app/seed.py

from app.database.session import SessionLocal
from app.models.role import Role
from app.models.user import User
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.core.security import hash_password


RESOURCES = [
    "users", "roles", "branches", "permissions",
    "categories", "products", "product_categories",
    "product_variants", "orders", "order_items", "user_branches"
]
ACTIONS = ["create", "read", "update", "delete"]

ROLES = ["admin", "manager", "staff"]

# Which actions each role gets, per resource. Applied uniformly across all resources for now.
ROLE_ACTIONS = {
    "admin": ["create", "read", "update", "delete"],
    "manager": ["create", "read", "update"],
    "staff": ["read"],
}


def get_or_create_role(db, name, description):
    role = db.query(Role).filter(Role.name == name).first()
    if not role:
        role = Role(name=name, description=description)
        db.add(role)
        db.commit()
        db.refresh(role)
        print(f"Created role: {role.name} (id={role.id})")
    else:
        print(f"Role already exists: {role.name} (id={role.id})")
    return role


def get_or_create_permission(db, name, description):
    perm = db.query(Permission).filter(Permission.name == name).first()
    if not perm:
        perm = Permission(name=name, description=description)
        db.add(perm)
        db.commit()
        db.refresh(perm)
    return perm


def link_role_permission(db, role_id, permission_id):
    exists = db.query(RolePermission).filter(
        RolePermission.role_id == role_id,
        RolePermission.permission_id == permission_id
    ).first()
    if not exists:
        db.add(RolePermission(role_id=role_id, permission_id=permission_id))


def seed():
    db = SessionLocal()

    try:
        # 1. Create roles
        role_objs = {}
        for role_name in ROLES:
            role_objs[role_name] = get_or_create_role(
                db, role_name, f"{role_name.capitalize()} role"
            )

        # 2. Create all permissions (resource:action)
        permission_objs = {}
        for resource in RESOURCES:
            for action in ACTIONS:
                perm_name = f"{resource}:{action}"
                permission_objs[perm_name] = get_or_create_permission(
                    db, perm_name, f"Can {action} {resource}"
                )
        db.commit()
        print(f"Ensured {len(permission_objs)} permissions exist")

        # 3. Link roles to permissions
        for role_name, allowed_actions in ROLE_ACTIONS.items():
            role = role_objs[role_name]
            for resource in RESOURCES:
                for action in allowed_actions:
                    perm_name = f"{resource}:{action}"
                    link_role_permission(db, role.id, permission_objs[perm_name].id)
        db.commit()
        print("Linked role-permission mappings")

        # 4. Create admin user
        admin_email = "admin@rbac.com"
        admin_user = db.query(User).filter(User.email == admin_email).first()

        if not admin_user:
            admin_user = User(
                name="Admin",
                email=admin_email,
                password=hash_password("Admin123!"),
                is_active=True,
                role_id=role_objs["admin"].id
            )
            db.add(admin_user)
            db.commit()
            db.refresh(admin_user)
            print(f"Created user: {admin_user.email} (id={admin_user.id})")
        else:
            print(f"User already exists: {admin_user.email} (id={admin_user.id})")

    finally:
        db.close()


if __name__ == "__main__":
    seed()