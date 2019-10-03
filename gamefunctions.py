import pygame
import sys
from ball import Ball
from playerone import PlayerSide

def check_keydown_ball(event, ball):
    if event.key == pygame.K_SPACE:
        ball.moving = 2


def check_keydown_player_one(event, player_one):
    if event.key == pygame.K_UP :
        player_one.moving_up = True
    elif event.key == pygame.K_DOWN:
        player_one.moving_down = True


def check_keydown_player_two(event, player_two):
    if event.key == pygame.K_w:
        player_two.moving_up = True
    elif event.key == pygame.K_s:
        player_two.moving_down = True


def check_keyup_player_one(event, player_one):
    if event.key == pygame.K_UP:
        player_one.moving_up = False
    elif event.key == pygame.K_DOWN:
        player_one.moving_down = False


def check_keyup_player_two(event, player_two):
    if event.key == pygame.K_w:
        player_two.moving_up = False
    elif event.key == pygame.K_s:
        player_two.moving_down = False




def check_event(player_one, player_two, ball):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_player_one(event, player_one)
        if event.type == pygame.KEYDOWN:
            check_keydown_player_two(event, player_two)
        if event.type == pygame.KEYUP:
            check_keyup_player_one(event, player_one)
        if event.type == pygame.KEYUP:
            check_keyup_player_two(event,player_two)
        if event.type == pygame.KEYDOWN:
            check_keydown_ball(event, ball)




def update_screen(screen, settings, player_one, player_two, ball):
    screen.fill(settings.rgb_color)
    ball.draw_ball()
    player_one.draw_player_one()
    player_two.draw_player_one()
    pygame.display.flip()

def update_ball(ball,player_two, player_one):
    if ball.rect.left >= 1200:
        ball.remove()
    if float(ball.rect.centerx) == float(player_two.rect.centerx ):
        ball.moving = 3
        ball.update(player_one)
