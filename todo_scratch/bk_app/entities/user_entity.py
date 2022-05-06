from todo_scratch.bk_base.auth.entities.auth_user_entity import AuthUserEntity


class UserEntity(AuthUserEntity):
    table_name = "user"

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def create_instance(user_name, email, password, is_admin):
        entity = UserEntity()
        entity.set_entity_values(user_name, email, password, is_admin)
        return entity
