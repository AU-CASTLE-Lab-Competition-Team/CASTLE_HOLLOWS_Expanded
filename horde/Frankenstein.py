import arcade
from .enemy import Enemy
from constants import FRANK_SPEED
from constants import FRANK_HEALTH
from constants import FRANK_MONEY

class Frankenstein(Enemy):
    def __init__(self, image, scale, position_list):
        super().__init__(image, scale, position_list)

        self.speed = FRANK_SPEED
        self.health = FRANK_HEALTH
        self.money = FRANK_MONEY

    def on_death(self):
        return True