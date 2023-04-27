import json

"""Track statistics for Alien Invasion"""
class GameStats:
    
    """Initialize the statistical information"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        # High score should never be reset.
        self.high_score = self.get_saved_high_score()

    """Initialize statistics that can change during the game"""    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    """Gets high score from file, if it exists"""
    def get_saved_high_score(self):
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0