from typing import Dict, List, Set
from xmlrpc.client import Boolean
from todo_scratch.bk_app.entities.group_belongs_entity import GroupBelongEntity
from todo_scratch.bk_app.entities.group_belongs_user_entity import GroupBelongsUserEntity
from todo_scratch.bk_app.entities.group_entity import GroupEntity
from todo_scratch.bk_app.entities.task_status_entity import TaskStatusEntity
from todo_scratch.bk_app.enums.group_auth_type_enum import GroupAuthTypeEnum
from todo_scratch.bk_app.enums.group_user_state_enum import GroupUserStateEnum
from todo_scratch.bk_app.repositories.group_repository import GroupRepository
from todo_scratch.bk_base.db.db_accesors.db_accesor import DbAccesor


class GroupHandler:
    """GroupControllerのハンドラクラス
    """

    def __init__(self) -> None:
        self.group_repository = GroupRepository()

    def is_join_to_group(self, user_id: int, group_id: int) -> Boolean:
        """グループに参加しているか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループID

        Returns:
            Boolean: グループの参加有無
        """
        group_belongs_entities = self.group_repository.get_group_belongs_by_id(
            user_id=user_id,
            group_id=group_id
        )
        if len(group_belongs_entities) <= 0:
            return False
        return group_belongs_entities[0].user_status.value == int(GroupUserStateEnum.APPROVED)

    def is_host_user_in_group(self, user_id: int, group_id: int) -> Boolean:
        """グループのホストユーザであるか判定

        Args:
            user_id (int): ユーザID
            group_id (int): グループiD

        Returns:
            Boolean: ホストユーザであるかの有無
        """
        group_belongs_entities = self.group_repository.get_group_belongs_by_id(
            user_id=user_id,
            group_id=group_id
        )
        if len(group_belongs_entities) <= 0:
            return False
        return group_belongs_entities[0].user_status.value == int(GroupUserStateEnum.APPROVED) and \
            group_belongs_entities[0].auth_type.value == int(GroupAuthTypeEnum.HOST)

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

        # 投稿ユーザの所属情報エンティティの作成
        post_user_group_belongs_entity = GroupBelongEntity.create_instance(
            insert_group_id,
            post_user_id,
            int(GroupAuthTypeEnum.HOST),  # ホストユーザ
            int(GroupUserStateEnum.APPROVED),  # 承認済み
        )

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

            #  招待ユーザのユーザ所属情報エンティティ作成
            group_belongs_entities.append(
                GroupBelongEntity.create_instance(
                    insert_group_id,
                    user_entities[0].user_id.value,
                    int(GroupAuthTypeEnum.NOMAL),  # 一般ユーザ
                    int(GroupUserStateEnum.UNAPPROVED),  # 未承認
                )
            )

        if len(group_belongs_entities) <= 0:
            return insert_group_id

        # 招待ユーザのユーザ所属情報の保存
        self.group_repository.save_group_belongs_list(group_belongs_entities)

        # グループのデフォルトのタスクステータス情報の保存
        task_status_entites = self._create_default_task_status_entities(insert_group_id)
        self.group_repository.save_task_status(task_status_entites)

        return insert_group_id

    def update_group_by_id(self, user_id: int, group_id: int, group_name: str, description: str):
        """グループ情報の更新

        Args:
            user_id (int): リクエストするユーザID
            group_id (int): グループID
            group_name (str): 変更後のグループ名
            description (str): 変更後のグループ説明分

        Returns:
            _type_: 変更したグループのID
        """
        selected_group_entities = self.group_repository.get_group_by_user_id(
            user_id=user_id,
            group_id=group_id
        )
        update_group_entity = selected_group_entities[0]

        update_group_entity.group_name.set_value(group_name)
        update_group_entity.description.set_value(description)

        self.group_repository.update_group(update_group_entity)

        return update_group_entity.group_id.value

    def update_or_save_group_belongs_by_user_dic(self, group_id: int, group_belongs_list: List[Dict]):
        """グループの所属情報の更新・追加
        既にあるユーザは更新、新規ユーザは追加する

        Args:
            group_id (int): 更新するグループのID
            group_belongs_list (List[Dict]): 更新後のグループ所属情報リスト
        """

        group_belongs_entities: List[GroupBelongEntity] = self.group_repository.get_group_belongs_by_group_id(group_id=group_id)
        if len(group_belongs_entities) <= 0:
            return

        db_accesor = DbAccesor(GroupBelongEntity)
        user_id_list: Set[int] = set()

        for group_belongs_entity in group_belongs_entities:
            is_update = False
            user_id_list.add(group_belongs_entity.user_id.value)

            for group_belongs in group_belongs_list:
                if group_belongs.get("user_id") == group_belongs_entity.user_id.value:
                    # 既存ユーザのグループ所属情報の更新
                    group_belongs_entity.auth_type.set_value(
                        int(GroupAuthTypeEnum.get_value(group_belongs.get("auth_type")))
                    )
                    is_update = True

            if is_update:
                db_accesor.update(group_belongs_entity)

        insert_group_belongs_entities: List[GroupBelongsUserEntity] = []
        for group_belongs in group_belongs_list:
            user_id = group_belongs.get("user_id")
            if user_id in user_id_list:
                continue

            # 新規ユーザのグループ情報の追加
            insert_group_belongs_entities.append(GroupBelongEntity.create_instance(
                group_id,
                user_id,
                int(GroupAuthTypeEnum.NOMAL),  # 一般ユーザ
                int(GroupUserStateEnum.UNAPPROVED),  # 未承認
            ))

        if len(insert_group_belongs_entities) > 0:
            self.group_repository.save_group_belongs_list(insert_group_belongs_entities)

    def update_group_belongs_by_user_status(self, user_id: int, group_id: int, user_status: GroupUserStateEnum) -> Boolean:
        """グループ所属情報の新規作成

        Args:
            user_id (int): ユーザID
            group_id (int): グループID
        """
        group_belongs_entities = self.group_repository.get_group_belongs_by_id(user_id, group_id)
        if len(group_belongs_entities) <= 0:
            return False

        update_entity = group_belongs_entities[0]
        update_entity.user_status.set_value(int(user_status))

        return self.group_repository.update_group_belongs(update_entity) > 0

    def get_detail_group_info(self, call_user_id: int, group_id: int) -> Dict:
        """指定したグループの詳細なグループ情報を取得します

        Args:
            group_id (int): グループID

        Returns:
            Dict: グループ情報
        """

        group_entity: GroupEntity = self.group_repository.get_group_entity_by_group_id(group_id)

        if group_entity is None:
            return {}

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
            if group_belong_user.user_id.value == call_user_id:
                call_user_auth_type = GroupAuthTypeEnum.get_value(group_belong_user.auth_type.value)
                call_user_user_state = GroupUserStateEnum.get_value(group_belong_user.user_status.value)

            group_belongs_users.append(group_belong_user.to_dict())

        group_detail_info["auth_type"] = int(call_user_auth_type)
        group_detail_info["user_state"] = int(call_user_user_state)
        group_detail_info["users"] = group_belongs_users

        task_status_entities = self.group_repository.get_task_status_by_group_id(
            group_id=group_entity.group_id.value
        )

        if len(task_status_entities) > 0:
            task_status_list: List = []
            for task_status_entity in task_status_entities:
                task_status_dict: Dict = {}
                task_status_dict["task_status_id"] = task_status_entity.task_status_id.value
                task_status_dict["task_status_name"] = task_status_entity.task_status_name.value
                task_status_dict["status_color"] = task_status_entity.status_color.value
                task_status_list.append(task_status_dict)

            group_detail_info["task_staus"] = task_status_list

        return group_detail_info

    def _create_default_task_status_entities(self, group_id: int) -> List[TaskStatusEntity]:
        task_staus_entities: List[TaskStatusEntity] = []
        task_staus_entities.append(TaskStatusEntity.create_instance(
            group_id,
            'Todo',
            '#EF7F74'
        ))
        task_staus_entities.append(TaskStatusEntity.create_instance(
            group_id,
            'Stay',
            '#EF7F74'
        ))
        task_staus_entities.append(TaskStatusEntity.create_instance(
            group_id,
            'Done',
            '#EF7F74'
        ))
        return task_staus_entities
