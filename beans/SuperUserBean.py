from beans.UserRepositoryBean import user_repository
from enums.RoleEnum import RoleEnum

super_user=user_repository.create_user(
    first_name="super",
    last_name="user",
    email="contollermanagement@superuser.com",
    organization_id=0,
    role_enum=RoleEnum.Admin
)