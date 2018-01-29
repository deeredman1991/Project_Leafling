""" This module holds the generic 'pile' class for storing piles
    of various things, such as food, on the ground.
"""

import math

import kivy.logger as logging

from scripts.sprite import Sprite

class Pile(Sprite):
    def __init__(self, name, contents_type, max_contents=math.inf,
                 spillage_recepticle=None, *args, **kwargs):
        img = 'images/pile.png'
        super(Pile, self).__init__( *args, source = img, **kwargs )

        self._max_contents = max_contents
        self._contents = max_contents if max_contents != math.inf else 0

        self._contents_type = contents_type

        self._spillage_recepticle = spillage_recepticle

        assert self._max_conents == math.inf or\
            self._spillage_recepticle is not None,\
                'Pile must either have a limit or a spillage recepticle.'

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, value):
        if value > self._max_contents:
            self.spill(value - self._max_contents)
            value = self._max_contents
        self._contents = value

    def spill(self, value):
        self._spillage_recepticle += value
