from typing import Any


class TestMainClass:
    def __init__(self) -> None:
        self.test = "test"


class TestMixin:
    def print(self,):
        if hasattr(self, 'test'):
            print(self.test)


class MergeClass(TestMixin, TestMainClass):
    pass


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
