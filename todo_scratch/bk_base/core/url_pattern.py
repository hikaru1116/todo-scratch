
import re
from typing import AnyStr, Pattern
from todo_scratch.bk_base.controller.controller import Controller


class UrlPattern:

    def __init__(self, path='^/$', controller: Controller = None) -> None:
        self.__path = path
        self.__path_compiled = re.compile(path)
        self.__controller = controller

    def get_path(self,) -> str:
        return self.__path

    def get_path_compiled(self,) -> Pattern[AnyStr]:
        return self.__path_compiled

    def get_controller(self,) -> Controller:
        return self.__controller
