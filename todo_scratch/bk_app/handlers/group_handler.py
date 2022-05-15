from typing import Dict, List
from todo_scratch.bk_app.entities.group_belongs_entity import GroupBelongEntity
from todo_scratch.bk_app.entities.group_belongs_user_entity import GroupBelongsUserEntity
from todo_scratch.bk_app.entities.group_entity import GroupEntity
from todo_scratch.bk_app.enums.group_auth_type_enum import GroupAuthTypeEnum
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository


class GroupHandler:
    """GroupControllerのハンドラクラス
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

    def get_group_entity_by_user_id(self, user_id: int) -> GroupEntity:

        return self.group_repository.get_group_entity_by_user_id(user_id)

    def create_group(self, group_info: Dict, post_user_id) -> int:
        """グループの新規作成処理

        Args:
            group_info (Dict): グループ作成情報
            post_user_id (_type_): 作成ユーザのユーザID

        Returns:
            int: 作成したグループのグループID
        """
        group_entity = GroupEntity.create_instance(
            group_name=group_info.get("group_name"),
            description=group_info.get("description")
        )

        insert_group_id = self.group_repository.save_group(group_entity)

        if insert_group_id <= 0:
            return 0

        post_user_group_belongs_entity = GroupBelongEntity.create_instance(
            insert_group_id,
            post_user_id,
            int(GroupAuthTypeEnum.HOST),  # ホストユーザ
            int(GroupUserStateEnum.APPROVED),  # 承認済み
            True  # 選択
        )

        # グループの選択を解除変更
        self.group_repository.update_group_selected(user_id=post_user_id, is_selected_off_only=True)

        # 投稿ユーザの所属情報の保存
        created_group_id = self.group_repository.save_group_belongs(post_user_group_belongs_entity)

        if created_group_id <= 0:
            return insert_group_id

        invite_users: Dict = group_info.get('invite_users', {})

        if len(invite_users) <= 0:
            return insert_group_id

        group_belongs_entities: List[GroupBelongEntity] = []
        for invite_user in invite_users:
            identifier = invite_user.get("identifier")
            if identifier is None:
                continue

            user_entities = self.group_repository.get_user_entity_by_identifier(identifier)

            if len(user_entities) <= 0 or user_entities[0].user_id.value == post_user_id:
                continue

            group_belongs_entities.append(
                GroupBelongEntity.create_instance(
                    insert_group_id,
                    user_entities[0].user_id.value,
                    int(GroupAuthTypeEnum.NOMAL),  # 一般ユーザ
                    int(GroupUserStateEnum.UNAPPROVED),  # 未承認
                    False  # 未選択
                )
            )

        if len(group_belongs_entities) <= 0:
            return insert_group_id

        # 招待ユーザのユーザ所属情報の保存
        self.group_repository.save_group_belongs_list(group_belongs_entities)

        return insert_group_id

    def get_detail_group_info(self, call_user_id: int, group_id: int) -> Dict:
        """指定したグループの詳細なグループ情報を取得します

        Args:
            group_id (int): グループID

        Returns:
            Dict: グループ情報
        """

        group_entity: GroupEntity = self.group_repository.get_group_entity(group_id)

        return self._create_detail_group_info_by_group_entity(
            user_id=call_user_id,
            group_entity=group_entity
        )

    def get_selected_detail_group_info(self, call_user_id) -> Dict:
        """選択済みの詳細なグループ情報を取得します

        Args:
            call_user_id (_type_): ユーザID

        Returns:
            Dict: グループ情報
        """
        group_entities: GroupEntity = self.group_repository.get_selected_group_by_user_id(
            user_id=call_user_id
        )

        if len(group_entities) <= 0:
            return {}

        return self._create_detail_group_info_by_group_entity(
            user_id=call_user_id,
            group_entity=group_entities[0]
        )

    def _create_detail_group_info_by_group_entity(self, user_id: int, group_entity: GroupEntity) -> Dict:
        group_belongs_user_entities: List[GroupBelongsUserEntity] \
            = self.group_repository.get_group_belongs_with_user_entities(group_entity.group_id.value)

        group_detail_info: Dict = {}

        group_detail_info["group_id"] = group_entity.group_id.value
        group_detail_info["group_name"] = group_entity.group_name.value
        group_detail_info["description"] = group_entity.description.value

        group_belongs_users: List = []

        call_user_auth_type = int(GroupAuthTypeEnum.NOMAL)
        call_user_user_state = int(GroupUserStateEnum.UNAPPROVED)
        for group_belong_user in group_belongs_user_entities:
            if group_belong_user.user_id.value == user_id:
                call_user_auth_type = GroupAuthTypeEnum.get_value(group_belong_user.auth_type.value)
                call_user_user_state = GroupUserStateEnum.get_value(group_belong_user.user_status.value)

            group_belongs_users.append(group_belong_user.to_dict())

        group_detail_info["auth_type"] = int(call_user_auth_type)
        group_detail_info["user_state"] = int(call_user_user_state)
        group_detail_info["users"] = group_belongs_users

        return group_detail_info
