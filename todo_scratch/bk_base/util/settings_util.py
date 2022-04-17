

import os
from importlib import import_module
from typing import cast


def get_settings():
    """設定ファイルを取得します

    Raises:
        Exception: _description_

    Returns:
        _type_: 設定ファイルモジュール
    """
    settings_path = os.environ.get('SETTINGS_PATH', None)
    if not settings_path:
        raise Exception
    settings_module = import_module(cast(str, settings_path))

    return settings_module
