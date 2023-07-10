import pygame
import sys
import game_functions as functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Initialize the game and make the window for it

    pygame.init()
    game_settings = Settings()
    window = pygame.display.set_mode((game_settings.window_width, game_settings.window_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(game_settings, window, "Play")
    
    spaceship = Ship(window, game_settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(game_settings)
    score = Scoreboard(game_settings, window, stats)

    functions.create_fleet(game_settings, window, spaceship, aliens)

    #Main loop of the game
    while True:

        functions.check_events(game_settings, window, stats, score, play_button, spaceship, aliens, bullets)

        if stats.game_running:

            spaceship.update()
            functions.update_bullets(game_settings, window, stats, score, spaceship, aliens, bullets)
            functions.update_aliens(game_settings, stats, score, window, spaceship, aliens, bullets)


        functions.update_screen(game_settings, window, stats, score, spaceship, bullets, aliens, play_button)
    
run_game()