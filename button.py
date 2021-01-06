import pygame.font
from enum import Enum

class ResetQuit(Enum):

    RESTART = 1
    QUIT = 2



class Button():

    def __init__(self, screen, side):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (30, 250, 30)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.
        if side == ResetQuit.RESTART:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center
        if side == ResetQuit.QUIT:
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.top = self.screen_rect.centery +100
            self.rect.left = self.screen_rect.centerx -100


        # The button message needs to be prepped only once.



    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
                                      self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

