class Settings():

    def __init__(self):
        '''Initialize the game's settings'''

        self.window_width = 1200
        self.window_height = 800
        self.background_color = (41,0,102)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3

        self.drop_speed = 10

        self.speed_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def speed_increase(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.fleet_direction *= self.speed_scale

        self.alien_points = int(self.alien_points * self.score_scale)