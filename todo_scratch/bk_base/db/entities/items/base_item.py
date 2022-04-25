

from abc import ABCMeta, abstractclassmethod
from typing import Dict


class BaseItem(metaclass=ABCMeta):

    value = None
    attribute: Dict = {}
    is_primary = False

    @abstractclassmethod
    def to_item(self):
        pass

    @abstractclassmethod
    def get_value(self,):
        pass

    @abstractclassmethod
    def validate(self,):
        pass

    @property
    def value(self):
        return self.value
