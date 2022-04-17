from typing import Any


class TestClass:
    """テスト用のクラス
    """

    def __init__(self) -> None:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """__call__メソッド

        Returns:
            Any: 数値
        """
        print('call TestClass')
        return 3

    @staticmethod
    def shori() -> str:
        """テスト用に文字列を返す

        Returns:
            str: テスト文字列
        """
        return 'TestClass'
