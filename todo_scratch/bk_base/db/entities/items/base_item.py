class BaseItem:

    _value = None

    @property
    def value(self,):
        return self._value

    def set_value(self, value):
        self._value = value

    @classmethod
    def to_item(self, data):
        raise NotImplementedError()

    def to_param(self):
        raise NotImplementedError()

    def validate(self,):
        raise NotImplementedError()
