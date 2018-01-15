from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.clock import Clock

from scripts.critter import Critter

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        
        self.critter = Critter()
        self.add_widget(self.critter)
        
        #self.critter.speak()
        
        #Clock.schedule_interval(self.update, 1.0/60.0)
        Clock.schedule_interval(self.update, 1.0/1)
        
    def update(self, dt):
        for child in self.children:
            child.update(dt)