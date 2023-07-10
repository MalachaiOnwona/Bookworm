import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, window, game_settings):

        super(Ship, self).__init__()

        self.window = window

        '''Loads the ship image and gets its rectangle, which will allow us to 
        use its x and y coordinates. We also get the rectangle of the game window''' 

        self.image = pygame.image.load('Alien Invasion/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.window_rectangle = window.get_rect()

        self.rect.centerx = self.window_rectangle.centerx
        self.rect.bottom = self.window_rectangle.bottom

        self.moving_right = False
        self.moving_left = False

        self.game_settings = game_settings
        self.center = float(self.rect.centerx)
    
    def update(self):
        if self.moving_right and self.rect.right < self.window_rectangle.right:
            self.center += self.game_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        self.rect.centerx = self.center

    
    def draw(self):
        #Draws the ship to it's current location
        
        self.window.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.window_rectangle.centerx