import pygame
import random
from ball import Ball

class SupriseBox():

    def __init__(self, screen, pos, col):
        self.color = col
        self.rect = pos
        self.screen = screen

        self.timer = pygame.time.get_ticks()
        self.clock = 0
        self.duration = 8000
        self.draw = False


    def box_clock(self):
        self.timer = pygame.time.get_ticks()

    def draw_box(self):
        pygame.draw.rect(self.screen , self.color, self.rect )


    def suprise_faster_player(self, settings, ball):
        if ball.direction == 1:
            if self.timer < self.clock:
                settings.playerright_speed += 1


        elif ball.direction == -1:
            if self.timer < self.clock:
                settings.playerleft_speed += 1


    def suprise_slow_player(self, settings, ball):
        if  ball.direction == 1:
            if self.timer < self.clock:
                settings.playerright_speed -= 1

        elif ball.direction == -1:
            if self.timer < self.clock:
                settings.playerleft_speed -= 1


    def suprise_small_player(self, settings, ball):
        if  ball.direction == 1:
            if self.timer < self.clock:
                settings.playerleft_height -= 50

        elif ball.direction == -1:
            if self.timer < self.clock:
                settings.playerright_height -= 50

    def suprise_large_player(self, settings, ball):
        if  ball.direction == -1:
            if self.timer < self.clock:
                settings.playerleft_height += 20

        elif ball.direction == 1:
            if self.timer < self.clock:
                settings.playerright_height += 20



