class BaseItem:

    _value = None
    _default_value = None

    @property
    def value(self,):
        return self._value

    def set_value(self, value):
        self._value = value
