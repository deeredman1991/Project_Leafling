from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock
import kivy.logger as logging

from scripts.critter import Critter

logger = logging.Logger

class Game(Widget):
    def __init__(self):
        logger.info('Game: Initializing - {0}.__init__()'.format(self))
        super(Game, self).__init__()
        
        logger.debug('Game: In: {0}.__init__() | templine #1'.format(self))
        self.critter = Critter('Fuzz')
        logger.debug('Game: In: {0}.__init__() | templine #2'.format(self))
        self.add_widget(self.critter)
        
        #print(self.critter.parent)
        
        #self.critter.speak()
        
        #Clock.schedule_interval(self.update, 1.0/60.0)
        #_timeout = 1.0/60.0
        _timeout = 1
        logger.debug('Game: In: {0}.__init__() | Declared - _timeout = {1}({2})'.format(self, type(_timeout), _timeout))
        
        logger.info('Game: In: {0}.__init__() | Scheduling - {1})'.format(self, Clock.schedule_interval(self.update, _timeout) ) )
        
    def update(self, dt):
        logger.info('Game: Running - {0}.update(self={0}, dt={1}({2}) )'.format(self, type(dt), dt))
        
        logger.debug('Game: In: {0}.update(dt={1}) | Iterating - {2}({3})'.format(self, dt, type(self.children), self.children))
        for child in self.children:
            logger.debug('Game: In: {0}.update(dt={1}) | Calling - {2}.update({1})'.format(self, dt, child))
            child.update(dt)