class GameStats():

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_running = False
        self.high_score = 0
    
    def reset_stats(self):
        self.num_ships_left = self.settings.ship_limit
        self.score = 0
        self.game_level = 1