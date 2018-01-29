""" Defines the Critter class for making critters

"""
import datetime

from kivy.core.window import Window
import kivy.logger as logging

from scripts.sprite import Sprite
from scripts.gui import Meter

logger = logging.Logger

class Critter(Sprite):
    def __init__(self, name):
        logger.info('Critter: Initializing - {0}.__init__( name={1}({2}) )'.format(self, type(name), name))

        _img = 'images/critter.png'

        logger.debug('Critter: In: {0}.__init__( name={1}({2}) ) | Calling - ' \
            'super(Critter, {0}).__init__(center={3}({4}), source={5}({6}))'.format( \
            self, type(name), name, type(Window.center), Window.center, type(_img), _img))
        super(Critter, self).__init__( center=Window.center, source=_img )

        self._name = name

        self._hunger = Meter( 'Hunger', 0 )
        self.add_widget( self._hunger )

        self._tiredness = Meter( 'Tiredness', 0 )
        #self.add_widget( self._tiredness )

        self._thirst = Meter( 'Thirst', 0 )
        #self.add_widget( self._thirst )

        self._happiness = Meter( 'Happiness', 0 )
        #self.add_widget( self._happiness )

        self._illnesses = []

        self._next_tick = datetime.datetime.now().replace( 
            second = (datetime.datetime.now().second+2)%60
        )

        logger.info("Critter: Initialized - {0}.__dict__ = {1}".format(self, self.__dict__))

    @property
    def name(self):
        return self._name

    @property
    def hunger(self):
        return self._hunger.value

    @hunger.setter
    def hunger(self, v):
        self._hunger.value = v

    @property
    def tiredness(self):
        return self._tiredness.value

    @tiredness.setter
    def tiredness(self, v):
        self._tiredness.value = v

    @property
    def thirst(self):
        return self._thirst.value

    @thirst.setter
    def thirst(self, v):
        self._thirst.value = v

    @property
    def happiness(self):
        return self._happiness.value

    @happiness.setter
    def happiness(self, v):
        self._happiness.value = v

    @property
    def illnesses(self):
        return self._illnesses

    def update(self, dt):
        for illness in self._illnesses:
            illness.update()


        #print(self._next_tick)
        #print(datetime.datetime.now())
        #print(datetime.datetime.now().second)
        #print('')

        #self.hunger += 1

        '''
        #TODO:
            Needs to queue up multiple ticks in case the player has skipped 
                multiple ticks while logged off.
        #FIXME:
            ALSO; there is a bug with %60... if (and only if) I have to do %60
                the minute attribute needs to increment...
        '''
        if self._next_tick <= datetime.datetime.now():
            self.speak()
            self._next_tick = self._next_tick.replace( 
                second = (self._next_tick.second+2)%60 
            )

        for child in self.children:
            child.update(dt)

    def speak(self, msg="Woof Woof!"):
        print(msg)
