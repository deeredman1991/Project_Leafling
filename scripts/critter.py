from kivy.core.window import Window
from scripts.sprite import Sprite

import datetime

class Critter(Sprite):
    def __init__(self):
        super(Critter, self).__init__(center=Window.center, source='images/critter.png')
        
        self._hunger = 0
        self._tiredness = 0
        self._thirst = 0
        self._happiness = 0
        
        self._illnesses = []
        
        self._next_tick = datetime.datetime.now().replace(second = (datetime.datetime.now().second+2)%60)
        
    @property
    def illnesses(self):
        return self._illnesses
        
    def update(self, dt):
        for illness in self.illnesses:
            illness.update()
            
        #print(self._next_tick)
        #print(datetime.datetime.now())
        #print(datetime.datetime.now().second)
        #print('')
            
        #TODO!!!
        #Needs to queue up multiple ticks in case the player has skipped multiple ticks while logged off
        #ALSO: there is a bug with %60... if (and only if) I have to do %60 the minute attribute needs to increment...
        if self._next_tick <= datetime.datetime.now():
            self.speak()
            self._next_tick = self._next_tick.replace(second = (datetime.datetime.now().second+2)%60)
            
    def speak(self, msg="Woof Woof!"):
        print(msg)
