import arcade
from enemy import Enemy
from constants import ZOMBIE_SPEED
from constants import ZOMBIE_MONEY

class Zombie(Enemy):
    def __init__(self, image, scale, position_list):
        super().__init__(image, scale, position_list)

        self.speed = ZOMBIE_SPEED
        self.health = 120
        self.money = ZOMBIE_MONEY
        
    def on_death(self):
        return True