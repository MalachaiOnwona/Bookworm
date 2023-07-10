import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, settings, window):
        super(Alien, self).__init__()

        self.window = window
        self.settings = settings

        self.image = pygame.image.load('Alien Invasion/alienspacecraft.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.xcoord = float(self.rect.x)

    
    def blitme(self):
        self.window.blit(self.image, self.rect)

    def check_edges(self):
        window_rect = self.window.get_rect()

        if self.rect.right >= window_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.xcoord += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.xcoord