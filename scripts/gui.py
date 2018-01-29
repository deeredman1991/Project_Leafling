from kivy.uix.widget import Widget
from kivy.uix.label import Label

from scripts.sprite import Sprite
from scripts.stat import Stat

class Meter(Widget):
    def __init__(self, name, value, max_value=10, **kwargs):
        super(Meter, self).__init__(**kwargs)
        
        self._stat = Stat(self, name, value, max_value)
        
        self.label = Label( 
            text=self._stat.name,
            font_name = 'fonts/PenguinAttack/PenguinAttack.ttf',
            font_size = 18
        )
        self.label.height = self.label.font_size
        self.label.width = self.label.font_size/2*len(self.label.text)
        #TODO: Do not hard code label.y
        self.label.y = 0
        self.add_widget(self.label)
        
        self.height = self.label.height
        
        self.pips = []
        
        self._draw_pips()
        
    @property
    def value(self):
        return self._stat.value
        
    @value.setter
    def value(self, v):
        self._stat.value = v
        self._draw_pips()
        
    @property
    def max_value(self):
        return self._stat.max_value
        
    @max_value.setter
    def max_value(self, v):
        self._stat.max_value = v
        
    def _draw_pips(self):
        for pip in self.pips:
            self.remove_widget( pip )
            
        for i in range(self.max_value):
            if i < self.value:
                self.pips.append( Sprite(source = 'images/pip.png') )
                
                self.pips[i].x = ( 
                    self.label.width+( (self.pips[i].width+5)*i ) )
                self.pips[i].y = self.y
                
                self.add_widget( self.pips[i] )
                
    def update(self, dt):
        self._draw_pips()