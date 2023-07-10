import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_settings, window, spaceship):
        super(Bullet,self).__init__()
        self.window = window

        self.rect = pygame.Rect(0,0,game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top

        self.ycoord = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    
    def update(self):
        self.ycoord -= self.speed_factor
        self.rect.y = self.ycoord

    def draw_bullet(self):
        pygame.draw.rect(self.window, self.color, self.rect)
