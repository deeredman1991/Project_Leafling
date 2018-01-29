import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class Stat(object):
    def __init__(self, parent, name, value, max_value, *args, **kwargs):
        logger.info("Stat class initialed. Stat({},{},{},{})".format( 
            parent, name, value, max_value)
        )
        
        logger.debug("Calling: super(Stat, self).__init__(")
        super(Stat, self).__init__(*args, **kwargs)
        
        self._name = name
        self._value = value
        self._max_value = max_value
        
        self.parent = parent
        
        logger.info("Stat: Initialized - {0}.__dict__ = {1}".format(self, self.__dict__))

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
        #TODO: Add docstring and doctest here...
        if v <= self._max_value:
            self._value = v
            return True
        elif v < 0:
            self._value = 0
            return False
        
        assert ( self._value >= 0 ) and ( self._value <= self._max_value ), \
            "{}'s {} cannot be {}. Value must be between 0 and {}.".format( 
                self.parent.parent.name, 
                self._name, 
                self._value, 
                self._max_value 
            )
        return False
