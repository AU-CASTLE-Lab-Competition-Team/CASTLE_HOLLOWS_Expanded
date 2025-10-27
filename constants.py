# Central file for global game constants

# Enemy (skeleton) settings
SPRITE_SCALING_ENEMY = 0.15
ENEMY_SPEED = 100

# Zombie settings
SPRITE_SCALING_ZOMBIE = 0.06
ZOMBIE_SPEED = 125

# Vampire settings
SPRITE_SCALING_VAMPIRE = 0.10
VAMPIRE_SPEED = 135

# Window settings
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "CASTLE HALLOWS"

# Colors, asset paths
BACKGROUND_COLOR = (169, 189, 224)  # arcade.color.GRAY_BLUE equivalent

# Seed/pumpkin stats
SEED_DAMAGE = 35
SEED_SPEED = 400
PUMP_RANGE = 200
FIRE_RATE = 100

#Gourd Stats
G_SEED_DAMAGE = 75
G_SEED_SPEED = 600
G_PUMP_RANGE = 700
G_FIRE_RATE = 150

#List of Pumpkin names to use for the shop
#Order of Dictionary: Name: [Purchase Cost, Upgrade Cost]
PUMPKIN_NAMES = ['classic','gourd']
PUMPKINS = {'classic':[5,3,SEED_DAMAGE,SEED_SPEED,PUMP_RANGE,FIRE_RATE],'gourd':[8,5,G_SEED_DAMAGE,G_SEED_SPEED,G_PUMP_RANGE,G_FIRE_RATE]}