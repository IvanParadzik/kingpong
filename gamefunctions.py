import pygame
import sys
from playerone import PlayerSide
from math import pi
import random
import pygame.time


def check_quit_restart_event(event, game, scoreboard_1, scoreboard_2):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            scoreboard_1.stats_left = 5
            scoreboard_2.stats_right = 5
            game.restart = False
        if event.key == pygame.K_q:
            game.run = False

def check_pause(event, game):
    if event.key == pygame.K_p:
        game.pause = True
        game.clock.wait()


    elif event.key == pygame.K_c:
        game.pause = False



def check_bash_down(event, player_one, player_two):
    if event.key == pygame.K_d:
        player_one.bash = True


    if event.key == pygame.K_LEFT:
        player_two.bash = True


def check_bash_up(event,player_one, player_two):
    if event.key == pygame.K_d:
        player_one.bash = False

    if event.key == pygame.K_LEFT:
        player_two.bash = False



def check_keydown_ball(event, ball, game, box_1, box_2, box_3):
    if event.key == pygame.K_SPACE:
        ball.moving = True
        game.state = False
        game.start = True
        box_1.clock = box_1.timer + box_1.duration
        box_2.clock = box_2.timer + box_2.duration
        box_3.clock = box_3.timer + box_3.duration





def check_keydown_player_one(event, player_one):
    if event.key == pygame.K_w :
        player_one.moving_up = True
    elif event.key == pygame.K_s:
        player_one.moving_down = True


def check_keydown_player_two(event, player_two):
    if event.key == pygame.K_UP:
        player_two.moving_up = True
    elif event.key == pygame.K_DOWN:
        player_two.moving_down = True


def check_keyup_player_one(event, player_one):
    if event.key == pygame.K_w:
        player_one.moving_up = False
    elif event.key == pygame.K_s:
        player_one.moving_down = False


def check_keyup_player_two(event, player_two):
    if event.key == pygame.K_UP:
        player_two.moving_up = False
    elif event.key == pygame.K_DOWN:
        player_two.moving_down = False


def check_pause_event(event, game):
    if event.type == pygame.KEYDOWN:
        check_pause(event, game)
    if event.type == pygame.KEYDOWN:
        check_pause(event, game)


def check_bash_event(event, player_one, player_two):
    if event.type == pygame.KEYDOWN:
        check_bash_down(event, player_one, player_two)
    if event.type == pygame.KEYUP:
        check_bash_up(event, player_one, player_two)


def check_player_event(event, player_one, player_two):
    if event.type == pygame.KEYDOWN:
        check_keydown_player_one(event, player_one)
    if event.type == pygame.KEYDOWN:
        check_keydown_player_two(event, player_two)
    if event.type == pygame.KEYUP:
        check_keyup_player_one(event, player_one)
    if event.type == pygame.KEYUP:
        check_keyup_player_two(event, player_two)


def check_ball_start_event(event, ball, game, box_1, box_2, box_3):
    if event.type == pygame.KEYDOWN:
        check_keydown_ball(event, ball, game, box_1, box_2, box_3)


#########################################################
def check_event(player_one, player_two, ball, game,scoreboard_1, scoreboard_2, box_1, box_2, box_3):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_player_event(event, player_one, player_two)
        check_ball_start_event(event, ball, game, box_1, box_2, box_3)
        check_pause_event(event, game)
        check_quit_restart_event(event, game, scoreboard_1, scoreboard_2 )
        check_bash_event(event, player_one, player_two)



def update_box_screen( box_1, box_2, box_3):

    if box_1.timer > box_1.clock:
        box_1.draw_box()
        box_1.draw = True
    else:
        box_1.draw = False

    if box_2.timer > box_2.clock:
        box_2.draw_box()
        box_2.draw = True
    else:
        box_2.draw = False

    if box_3.timer > box_3.clock:
        box_3.draw_box()
        box_3.draw = True
    else:
        box_3.draw = False



def update_score_screen(game, scoreboard_1, scoreboard_2):
    if game.start:
        scoreboard_1.draw_score(PlayerSide.LEFT)
        scoreboard_2.draw_score(PlayerSide.RIGHT)


def update_restart_quit(game, restart_button, quit_button):
    if game.restart:
        restart_button.draw_button()
        quit_button.draw_button()


def update_player_button(game, play_button):
    if not game.start:
        play_button.draw_button()


def update_start_screen(screen, settings, player_one, player_two, ball, play_button,restart_button, quit_button, game,scoreboard_1, scoreboard_2):

    screen.fill(settings.rgb_color)
    update_score_screen(game, scoreboard_1, scoreboard_2)
    update_player_button(game, play_button)
    update_restart_quit(game, restart_button, quit_button)
    ball.draw_ball()
    player_one.draw_player_one()
    player_two.draw_player_one()
    pygame.display.flip()

#####################################################################################################################################
def update_screen(screen, settings, player_one, player_two, ball,scoreboard_1, scoreboard_2, game, box_1, box_2 , box_3):

    screen.fill(settings.rgb_color)
    update_score_screen(game, scoreboard_1, scoreboard_2)
    update_box_screen( box_1, box_2, box_3)

    ball.draw_ball()
    player_one.draw_player_one()
    player_two.draw_player_one()
    pygame.display.flip()


################################################################################
def check_collision_player( ball, side,player_two, player_one , settings):
    if side == PlayerSide.RIGHT:
        if ball.pos[0] + ball.r > player_two.rect.left:
            if int(ball.pos[1]) in range(player_two.rect.top - ball.r, player_two.rect.bottom  + ball.r):
                if int(ball.pos[1]) < player_two.rect.centery:
                    ball.angle = (((player_two.rect.centery -player_two.rect.top + ball.r )- (ball.pos[1]- player_two.rect.top + ball.r))/(player_two.rect.centery -player_two.rect.top + ball.r ))* pi/3
                    ball.direction = 1
                    ball.check = True
                    settings.ball_speed += 0.05
                elif int(ball.pos[1]) > player_two.rect.centery:
                    ball.angle= -((ball.pos[1] - player_two.rect.centery)/(player_two.rect.bottom + ball.r -player_two.rect.centery))*pi/3
                    ball.direction = 1
                    ball.check = True
                    settings.ball_speed += 0.05
                elif int(ball.pos[1]) == player_two.rect.centery:
                    ball.angle = 0
                    ball.turn = -1
                    ball.check = True
                    settings.ball_speed += 0.05
            if player_one.bash_succeed:
                settings.ball_speed += 0.1
    if side == PlayerSide.LEFT:
        if ball.pos[0] - ball.r < player_one.rect.right:
            if int(ball.pos[1]) in range(player_one.rect.top - ball.r, player_one.rect.bottom  + ball.r):
                if int(ball.pos[1]) < player_one.rect.centery:
                    ball.angle = (((player_one.rect.centery -player_one.rect.top + ball.r )- (ball.pos[1]- player_one.rect.top + ball.r))/(player_one.rect.centery -player_one.rect.top + ball.r ))* pi/3
                    ball.direction = -1
                    ball.check = True
                    settings.ball_speed += 0.05
                elif int(ball.pos[1]) > player_one.rect.centery:
                    ball.angle = -((ball.pos[1] - player_one.rect.centery)/(player_one.rect.bottom + ball.r -player_one.rect.centery))*pi/3
                    ball.direction = -1
                    ball.check = True
                    settings.ball_speed += 0.05
                elif int(ball.pos[1]) == player_one.rect.centery:
                    ball.angle = 0
                    ball.turn = 1
                    ball.check = True
                    settings.ball_speed += 0.05
            if player_one.bash_succeed:
                settings.ball_speed += 0.1




def check_collision_down_up(ball,screen):
    screen_rect = screen.get_rect()
    if ball.pos[1]-20 < screen_rect.top and ball.check == False:
        ball.check = True
    elif ball.pos[1] - 20 < screen_rect.top:
        ball.check = False
    if ball.pos[1] +20> screen_rect.bottom and ball.check == False:
        ball.check = True
    elif ball.pos[1] +20 > screen_rect.bottom:
        ball.check = False


###########################################################3
def refresh_all(ball ,settings, screen, player_one, player_two ):
    screen_rect = screen.get_rect()
    ball.turn = -1
    settings.ball_speed = 2
    settings.playerleft_speed = 2
    settings.playerright_speed = 2
    settings.playerleft_height = 200
    settings.playerright_height = 200
    player_one.rect.centery = screen_rect.centery
    player_two.rect.centery = screen_rect.centery





def check_score(ball,screen,game ,scoreboard_1, scoreboard_2, settings, player_one, player_two):
    screen_rect = screen.get_rect()
    if ball.pos[0] > screen_rect.right -20:
        refresh_all(ball, settings,screen, player_one, player_two)
        scoreboard_2.stats_right -= 1
        game.servis = PlayerSide.RIGHT
        game.state = True
        if scoreboard_2.stats_right == 0:
            game.restart = True

    elif ball.pos[0]< screen_rect.left +20:
        refresh_all(ball, settings,screen, player_one, player_two)
        scoreboard_1.stats_left -= 1
        game.servis = PlayerSide.LEFT
        game.state = True
        if  scoreboard_1.stats_left == 0:
            game.restart = True



def check_suprise(settings, ball, box_1, box_2 , box_3):
    if box_1.draw:
        check_suprise_box_1( box_1, settings,  ball)
    if box_2.draw:
        check_suprise_box_2(box_2, settings, ball)
    if box_3.draw:
        check_suprise_box_3(box_3, settings, ball)


def box_timer(box_1, box_2, box_3):
    box_1.box_clock()
    box_2.box_clock()
    box_3.box_clock()

()


def random_suprises_box_1(box_1, settings,ball):
    list_suprises_box_1 = [box_1.suprise_faster_player, box_1.suprise_large_player, box_1.suprise_small_player, box_1.suprise_large_player]
    random.choice(list_suprises_box_1)( settings, ball)

def random_suprises_box_2(box_2, settings,ball):
    list_suprises_box_2 = [box_2.suprise_faster_player, box_2.suprise_large_player, box_2.suprise_small_player, box_2.suprise_large_player]
    random.choice(list_suprises_box_2)( settings, ball)
def random_suprises_box_3(box_3, settings,ball):
    list_suprises_box_3 = [box_3.suprise_faster_player, box_3.suprise_large_player, box_3.suprise_small_player, box_3.suprise_large_player]
    random.choice(list_suprises_box_3)(settings, ball)




def check_suprise_box_1(box_1, settings, ball):
    if int(ball.pos[0] - ball.r) in range(int(box_1.rect[0]), int(box_1.rect[0] + 50)) or int(
            ball.pos[0] + ball.r) in range(int(box_1.rect[0]), int(box_1.rect[0] + 50)):
        if int(ball.pos[1]) in range(int(box_1.rect[1] - ball.r), int(box_1.rect[1] + 50 + ball.r)):
            box_1.clock = box_1.timer + box_1.duration
            random_suprises_box_1(box_1, settings, ball)



def check_suprise_box_2(box_2, settings, ball):
    if int(ball.pos[0]-ball.r)  in range( int(box_2.rect[0]), int(box_2.rect[0]+ 50) ) or int(ball.pos[0] + ball.r) in range(int(box_2.rect[0]), int(box_2.rect[0]+ 50)):
        if int(ball.pos[1]) in range(int(box_2.rect[1] - ball.r), int(box_2.rect[1] + 50 + ball.r)):
            box_2.clock = box_2.timer + box_2.duration
            random_suprises_box_2(box_2, settings, ball)


def check_suprise_box_3(box_3, settings, ball):
    if int(ball.pos[0] - ball.r) in range(int(box_3.rect[0]), int(box_3.rect[0] + 50)) or int(
            ball.pos[0] + ball.r) in range(int(box_3.rect[0]), int(box_3.rect[0] + 50)):
        if int(ball.pos[1]) in range(int(box_3.rect[1] - ball.r), int(box_3.rect[1] + 50 + ball.r)):
            box_3.clock = box_3.timer + box_3.duration
            random_suprises_box_3(box_3, settings, ball)






