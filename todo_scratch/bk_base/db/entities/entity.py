from abc import ABCMeta
from typing import List


class Entity(metaclass=ABCMeta):

    @classmethod
    def create_instance(cls):
        pass

    @classmethod
    def convert_to_entity(cls,):
        """Queryの結果をentityへ変換
        """
        for key, value in cls.__dict__.items():
            print(key, ':', value)

    @classmethod
    def convert_to_entity_list(self,) -> List:
        pass

    def convert_to_param(self,):
        """Entityをパラメータへ変換
        """
        pass

    def validate(self,):
        pass
