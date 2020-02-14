import pygame
from math import sin, cos, pi, tan
from playerone import PlayerSide
from pygame.sprite import Sprite
from playerone import Player
from enum import Enum
from pygame.sprite import Sprite

class GameState(Enum):
    START = 1
    INGAME = 2
    PAUSE = 3


class Ball():

    def __init__(self,screen, settings, side, start_pos, player_one,player_two, r = 20, ):
        self.pos = start_pos
        self.settings = settings
        self.side = side
        self.r = r

        self.screen = screen

        if side == PlayerSide.LEFT:
           self.pos = (player_one.rect.right + self.r, player_one.rect.centery)

        elif side == PlayerSide.RIGHT:
            self.pos = (player_two.rect.left - self.r, player_two.rect.centery)

        self.color = settings.ball_color
        self.speed = settings.ball_speed
        self.direction = 1

        self.moving = False
        self.angle = 0
        self.check = True
        self.turn = 1


    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, (int(self.pos[0]),int(self.pos[1])) , self.r)

    def ball_position(self, state, player_one,player_two, side, settings,game):
        if state == GameState.START:
            if side== PlayerSide.LEFT:
                self.pos = (player_one.rect.right + self.r, player_one.rect.centery)
            elif side == PlayerSide.RIGHT:
                self.pos = (player_two.rect.left - self.r, player_two.rect.centery)


        if state == GameState.INGAME:
            if not game.pause:
                if self.check:
                    if self.moving == True:
                        if self.angle == 0:
                            self.pos = (self.pos[0] + settings.ball_speed*self.turn) , self.pos[1]
                        if self.angle > 0:
                            x = ((self.pos[0] - settings.ball_speed* cos(self.angle)*self.direction))
                            y = ((self.pos[1] - settings.ball_speed*sin(self.angle)))
                            self.pos = x, y
                        elif self.angle < 0:
                            x = (self.pos[0] - settings.ball_speed * cos(self.angle)* self.direction)
                            y = (self.pos[1] - (settings.ball_speed * sin(self.angle)))
                            self.pos = x, y
                else:
                    if self.moving == True:
                        if self.angle == 0:
                            self.pos = self.pos[0] + settings.ball_speed, self.pos[1]

                        if self.angle > 0:
                            x = ((self.pos[0] - settings.ball_speed* cos(self.angle)*self.direction))
                            y = ((self.pos[1] + settings.ball_speed*sin(self.angle)))
                            self.pos = x, y
                        elif self.angle < 0:
                            x = (self.pos[0] - settings.ball_speed * cos(self.angle)* self.direction)
                            y = (self.pos[1] + (settings.ball_speed* sin(self.angle)))
                            self.pos = x, y


