import sys
from importlib import import_module
from importlib.abc import MetaPathFinder
from importlib.util import spec_from_file_location
from typing import Any


def import_module_member_from_file_route(member_name: str, route: str) -> Any:
    """モジュールルートから動的にモジュールをimportし、メンバーを取得します

    Args:
        member_name (str): メンバー変数名
        route (str): ルート

    Returns:
        Any: メンバー
    """
    module = import_module(route)
    member = getattr(module, member_name, None)
    return member


def import_module_from_file_location(name, location):
    """ファイルパスから動的にモジュールをimportします

    Args:
        name (_type_): importモジュール名
        location (_type_): ファイルパス

    Returns:
        _type_: importモジュール
    """
    class Finder(MetaPathFinder):
        @staticmethod
        def find_spec(fullname, *_):
            if fullname == name:
                return spec_from_file_location(name, location)

    finder = Finder()
    sys.meta_path.insert(0, finder)
    try:
        return import_module(name)
    finally:
        sys.meta_path.remove(finder)
