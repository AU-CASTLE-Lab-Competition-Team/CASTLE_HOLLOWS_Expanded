import arcade
import random
from enemy import Enemy
from bat import Bat
from constants import VAMPIRE_SPEED, BAT_COUNT

class Vampire(Enemy):
    def __init__(self, image, scale, position_list):
        super().__init__(image, scale, position_list)

        self.speed = VAMPIRE_SPEED
        self.health = 150
        self.enemy_list = None
        
    def on_death(self):
        image = "assets/images/bat.png"
        bat_position_list = [[1454, 800]]
        total_bats = BAT_COUNT
        for i in range(total_bats):
            rand_offset_x = random.randint(0,50)
            rand_offset_y = random.randint(0,50)
            bat = Bat(image,1, bat_position_list)
            if i % 2 == 0:
                bat.center_x = self.center_x + rand_offset_x
                bat.center_y = self.center_y + rand_offset_y
            else:
                bat.center_x = self.center_x - rand_offset_x
                bat.center_y = self.center_y - rand_offset_y
            self.enemy_list.append(bat)
        return f'Vampire death, spawn bats! Location: {self.center_x},{self.center_y}'