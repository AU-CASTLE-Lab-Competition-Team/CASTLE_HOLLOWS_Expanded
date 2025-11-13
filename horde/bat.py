import arcade
from .enemy import Enemy
from constants import BAT_SPEED, BAT_MONEY

class Bat(Enemy):
    def __init__(self, image, scale, position_list):
        super().__init__(image, scale, position_list)

        self.speed = BAT_SPEED
        self.health = 20
        self.money = BAT_MONEY
        
    def on_death(self):
        return True