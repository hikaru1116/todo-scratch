from enum import IntFlag


class GroupUserStateEnum(IntFlag):
    """グループのユーザの状態を表すENUM

    Args:
        IntFlag (_type_): Enum
    """
    UNAPPROVED = 0  # 未承認
    APPROVED = 1  # 承認済み
