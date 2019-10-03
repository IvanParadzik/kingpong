import pygame
import sys
from settings import Settings
from playerone import Player, PlayerSide
import gamefunctions as gf
from ball import Ball



def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('King Pong')

    player_one = Player(settings, screen, PlayerSide.LEFT)
    player_two = Player(settings, screen, PlayerSide.RIGHT)
    ball = Ball(screen, settings, PlayerSide.LEFT, player_one, player_two)


    while True:

        gf.check_event(player_one, player_two, ball)
        player_one.update_player(settings)
        player_two.update_player(settings)
        ball.update(player_one)
        print(ball.rect.centerx)
        print(player_two.rect.centerx)
        gf.update_ball(ball,player_two, player_one)
        gf.update_screen(screen, settings, player_one, player_two, ball)


run_game()


