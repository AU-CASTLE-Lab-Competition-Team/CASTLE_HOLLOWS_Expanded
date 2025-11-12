import arcade
from enemy import Enemy
from constants import BAT_SPEED

class Bat(Enemy):
    def __init__(self, image, scale, position_list):
        super().__init__(image, scale, position_list)

        self.speed = BAT_SPEED
        self.health = 20
        
    def on_death(self):
        return True