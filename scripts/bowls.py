
import kivy.logger as logging

from scripts.sprite import Sprite
from scripts.pile import Pile

logger = logging.Logger

class FoodBowl(Pile):
    def __init__(self, name, contents_type, *args, **kwargs):
        img = 'images/bowl.png'

        super(FoodBowl, self).__init__(*args,
                                   'Food Bowl',
                                   'food',
                                   max_contents = 100,
                                   source = img,
                                   spillage_recepticle = Pile('Floor Pile',
                                                              'food')
                                   **kwargs)
