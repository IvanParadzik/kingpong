import pygame

from playerone import PlayerSide
from pygame.sprite import Sprite
from playerone import Player
from enum import Enum


class Game_state(Enum):
    START = 1
    INGAME = 2
    PAUSE = 3


class Ball():

    def __init__(self, screen, settings, side,player_one, player_two):

        self.screen = screen
        self.settings = settings
        self.side = side
        self.rect = pygame.Rect(0, 0, 20, 20)
        if side == PlayerSide.LEFT:
            self.rect.centery = player_one.rect.centery
            self.rect.left = player_one.rect.left
        elif side == PlayerSide.RIGHT:
            self.rect.centery = player_two.rect.centery
            self.rect.right = player_two.rect.right

        self.x = float(self.rect.x)
        self.radius = settings.ball_radius
        self.color = settings.ball_color
        self.speed = settings.ball_speed

        self.moving = 1

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), self.radius)

    def update(self,player_one):
        if self.moving == 2:
            self.x += self.speed
            self.rect.x = self.x
        elif self.moving == 1:
            self.rect.x = player_one.rect.centerx
            self.rect.y = player_one.rect.centery
        elif self.moving == 3:
            self.x -= self.speed
            self.rect.x = self.x




    def update1(self):
        self.moving = 3
        self.x -= self.speed
        self.rect.x = self.x
