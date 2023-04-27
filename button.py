import pygame.font

class Button:
    """Initialize button attributes"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (102, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)

    """Turn msg into a rendered image and center text on the button"""
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    """Draw blank button and then draw message"""
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    """If the button has been moved, the text needs to be moved as well"""
    def _update_msg_position(self):
        self.msg_image_rect.center = self.rect.center