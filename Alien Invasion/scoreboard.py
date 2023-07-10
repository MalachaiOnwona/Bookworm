import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():

    def __init__(self, settings, window, stats):
        self.window = window
        self.window_rect = window.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        score_rounded = int(round(self.stats.score, -1))
        score_string = "{:,}".format(score_rounded)

        self.score_img = self.font.render(score_string, True, self.text_color, self.settings.background_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.window_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        string_high_score = "{:,}".format(high_score)

        self.high_score_img = self.font.render(string_high_score, True, self.text_color, self.settings.background_color)

        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.window_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.game_level), True, self.text_color, self.settings.background_color)

        self.level_rect = self. level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()

        for ship_num in range(self.stats.num_ships_left):
            ship = Ship(self.window, self.settings)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def display_score(self):
        self.window.blit(self.score_img, self.score_rect)
        self.window.blit(self.high_score_img, self.high_score_rect)
        self.window.blit(self.level_img, self.level_rect)
        self.ships.draw(self.window)