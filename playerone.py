import pygame

from enum import Enum
import pygame.time
from time import sleep
from math import pi
class PlayerSide(Enum):
    LEFT = 1
    RIGHT = 2


class Player():

    def __init__(self, settings, screen, side):
        self.side = side

        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        if side == PlayerSide.LEFT:
            self.rect = pygame.Rect(0, 0, settings.playerleft_width, settings.playerleft_height)
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.left
        elif side == PlayerSide.RIGHT:
            self.rect = pygame.Rect(0, 0, settings.playerright_width, settings.playerright_height)
            self.rect.centery = self.screen_rect.centery
            self.rect.right = self.screen_rect.right

        self.color = settings.player_color
        self.moving_down = False
        self.moving_up = False
        self.bash = False
        self.side = side
        self.bash_succeed = True
        self.bash_time = 500


    def draw_player_one(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update_player_height(self,settings, side):
        if side == PlayerSide.RIGHT:
            self.rect[3] = settings.playerright_height
        if side == PlayerSide.LEFT:
            self.rect[3] = settings.playerleft_height



    def update_player(self, settings,side, game):
        if not game.pause:
            if side == PlayerSide.LEFT:
                if self.bash:
                    if self.rect.right < 60:
                        self.rect.right += 30
                        self.bash_succeed = True
                else:
                    self.bash_succeed = False
                    self.rect.left = self.screen_rect.left
                    if self.moving_down:

                        if self.rect.centery < settings.screen_height -(settings.playerleft_height/2):
                            self.rect.centery += settings.playerleft_speed
                            self.rect.y += settings.playerleft_speed
                    if self.moving_up:
                        if self.rect.centery > settings.playerleft_height/2:

                            self.rect.centery -= settings.playerleft_speed
                            self.rect.y -= settings.playerleft_speed

            if side == PlayerSide.RIGHT:
                if self.bash:
                    if self.rect.left > 1140:
                        self.rect.left -= 30
                        self.bash_succeed = True
                else:
                    self.bash_succeed = False
                    self.rect.right = self.screen_rect.right
                    if self.moving_down:
                        if self.rect.centery < settings.screen_height -(settings.playerright_height/2):
                            self.rect.centery += settings.playerright_speed
                            self.rect.y += settings.playerright_speed
                    if self.moving_up:
                        if self.rect.centery > settings.playerright_height/2:
                            self.rect.centery -= settings.playerright_speed
                            self.rect.y -= settings.playerright_speed













