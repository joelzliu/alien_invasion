import pygame
from pygame.sprite import Sprite

""""A class to manage the ship"""
class Ship(Sprite):
    
    """Initialize the ship and set its starting position."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float number for the ship's attribtues
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    """Adjust the ship's position based on the moving sign"""
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # set current position
        # but self.rect.x only stores the integer part
        self.rect.x = self.x
        self.rect.y = self.y

    """Draw the ship at assigned location"""
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    """Center bottom the ship"""
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)