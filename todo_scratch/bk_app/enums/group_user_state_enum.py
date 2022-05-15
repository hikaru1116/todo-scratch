from enum import IntFlag


class GroupUserStateEnum(IntFlag):
    """グループのユーザの状態を表すENUM

    Args:
        IntFlag (_type_): Enum
    """
    UNAPPROVED = 0  # 未承認
    APPROVED = 1  # 承認済み

    @staticmethod
    def get_value(num: int):
        if num == int(GroupUserStateEnum.UNAPPROVED):
            return GroupUserStateEnum.UNAPPROVED
        elif num == int(GroupUserStateEnum.APPROVED):
            return GroupUserStateEnum.APPROVED
        else:
            return GroupUserStateEnum.UNAPPROVED
