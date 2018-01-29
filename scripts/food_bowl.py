
import kivy.logger as logging

from scripts.sprite import Sprite
from scripts.pile import Pile

logger = logging.Logger

class FoodBowl(Pile):
    def __init__(self, *args, **kwargs):
        img = 'images/food_bowl.png'

        super(FoodBowl, self).__init__(*args,
                                   'Food Bowl',
                                   'food',
                                   max_contents = 100,
                                   source = img,
                                   spillage_recepticle = Pile('Spilled Food',
                                                              'food')
                                   **kwargs)

class WaterBowl(Pile):
    def __init__(self, *args, **kwargs):
       img = 'images/water_bowl.png'

       super(WaterBowl, self).__init__(*args,
                                       'Water Bowl'
                                       'water',
                                       max_contents = 100,
                                       source = img,
                                       spillage_recepticle = Pile('Puddle of '\
                                                                  'Water',
                                                                  'water')
                                        **kwargs)
