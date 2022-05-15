from enum import IntFlag


class GroupAuthTypeEnum(IntFlag):
    """グループのユーザ権限を表すENUM

    Args:
        IntFlag (_type_): Enum
    """
    HOST = 0  # ホストユーザ
    NOMAL = 1  # 一般ユーザ

    @staticmethod
    def get_value(num: int):
        if num == int(GroupAuthTypeEnum.HOST):
            return GroupAuthTypeEnum.HOST
        elif num == int(GroupAuthTypeEnum.NOMAL):
            return GroupAuthTypeEnum.NOMAL
        else:
            return GroupAuthTypeEnum.NOMAL
