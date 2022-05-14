from enum import IntFlag


class GroupAuthTypeEnum(IntFlag):
    """グループのユーザ権限を表すENUM

    Args:
        IntFlag (_type_): Enum
    """
    HOST = 0  # ホストユーザ
    NOMAL = 1  # 一般ユーザ
