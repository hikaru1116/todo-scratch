from typing import Dict, List
from todo_scratch.bk_app.entities.group_belongs_entity import GroupBelongEntity
from todo_scratch.bk_app.entities.group_entity import GroupEntity
from todo_scratch.bk_app.enums.group_auth_type_enum import GroupAuthTypeEnum
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository


class GroupHandler:
    """GroupControllerのハンドラクラス
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

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
            int(GroupUserStateEnum.APPROVED)  # 承認済み
        )

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
                    int(GroupUserStateEnum.UNAPPROVED)  # 未承認
                )
            )

        if len(group_belongs_entities) <= 0:
            return insert_group_id

        self.group_repository.save_group_belongs_list(group_belongs_entities)

        return insert_group_id

    def get_detail_group_info(self, group_id: int) -> Dict:
        """詳細なグループ情報を取得します

        Args:
            group_id (int): グループID

        Returns:
            Dict: グループ情報
        """

        group_entity: GroupEntity = self.group_repository.get_group_entity(group_id)
        group_entity_dic = group_entity.to_dict()

        group_belongs_user_entities = self.group_repository.get_group_belongs_with_user_entities(group_id)

        group_detail_info: Dict = {}

        group_detail_info["group_id"] = group_entity_dic.get("group_id")
        group_detail_info["group_name"] = group_entity_dic.get("group_name")
        group_detail_info["description"] = group_entity_dic.get("description")
        group_belongs_users: List = []
        for group_belong_user in group_belongs_user_entities:
            group_belongs_users.append(group_belong_user.to_dict())

        group_detail_info["users"] = group_belongs_users
        return group_detail_info
