from abc import ABC, abstractclassmethod
from typing import Dict, Tuple, Callable


class Controller(ABC):
    """コントローラー基底クラス

    Args:
        ABC (_type_): 抽象クラス
    """

    @abstractclassmethod
    def dispatch(self, path=None, method="GET") -> Tuple[Callable, Dict]:
        """コールバック取得

        Returns:
            Tuple[Response, Dict]: レスポンス、レスポンス引数

        Returns:
            Tuple[Callable, Dict]: コールバック,コールバック引数
        """
        raise NotImplementedError
