
class Stat(object):
    def __init__(self, parent, name, value, max_value, **kwargs):
        super(Stat, self).__init__(**kwargs)
        
        self._name = name
        self._value = value
        self._max_value = max_value
        
        self.parent = parent
        
    @property
    def name(self):
        return self._name
        
    @property
    def max_value(self):
        return self._max_value
        
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, v):
        if v <= self._max_value:
            self._value = v
        elif v < 0:
            self._value = 0
        
        self._value = v
        assert ( self._value >= 0 ) and ( self._value <= self._max_value ), \
            "{}'s {} cannot be {}. Value must be between 0 and {}.".format( self.parent.parent.name, self._name, self._value, self._max_value )
        