import pygame
import  sys
from settings import Settings
from playerone import Player, PlayerSide
import gamefunctions as gf
from ball import Ball
from ball import GameState
from scoreboard import ScoreBoard
from button import Button
from suprise import SupriseBox
from pygame.sprite import Group
from button import ResetQuit


class Game():

    def __init__(self, state, servis):
        self.run = True
        self.state = state
        self.state = True
        self.servis = servis
        self.servis =PlayerSide.LEFT
        self.start = False
        self.counter = 0
        self.pause = False
        self.restart = False

        pygame.init()
        pygame.display.set_caption('King Pong')



    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return False
            settings = Settings()
            screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
            start_button = Button(screen, ResetQuit.RESTART)
            print(start_button.rect)
            start_button.prep_msg('Start')
            screen.fill(settings.rgb_color)
            start_button.draw_button()
            pygame.display.flip()

    def run_game(self):

        settings = Settings()
        screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        scoreboard_1 = ScoreBoard(screen, settings, PlayerSide.LEFT)
        scoreboard_2 = ScoreBoard(screen, settings, PlayerSide.RIGHT)
        screen_rect = screen.get_rect()
        player_one = Player(settings, screen, PlayerSide.LEFT)
        player_two = Player(settings, screen, PlayerSide.RIGHT)
        ball = Ball(screen, settings, PlayerSide.LEFT , (screen_rect.centerx, screen_rect.centery), player_one, player_two)


        box_top = screen_rect.centerx - 25, screen_rect.top + 150, 50, 50
        box_mid = screen_rect.centerx - 25, screen_rect.centery - 25, 50, 50
        box_down = screen_rect.centerx - 25, screen_rect.top + 500, 50, 50
        box_1 = SupriseBox(screen, box_top, (50, 50, 50))
        box_2 = SupriseBox(screen, box_mid, (100, 0, 0))
        box_3 = SupriseBox(screen, box_down , (0, 0, 100))


        while self.run :
            if self.state:

                player_one.update_player(settings, PlayerSide.LEFT, game)
                player_two.update_player(settings, PlayerSide.RIGHT, game)

                gf.check_event(player_one, player_two, ball, game,scoreboard_1, scoreboard_2, box_1, box_2, box_3)

                play_button = Button(screen, ResetQuit.RESTART)
                play_button.prep_msg('Left Player: [SPACE]')
                restart_button = Button(screen, ResetQuit.RESTART)
                restart_button.prep_msg('Press 'R' for Restart')
                quit_button = Button(screen, ResetQuit.QUIT)
                quit_button.prep_msg("Press 'Q' to Quit")

                scoreboard_1.score(PlayerSide.LEFT)
                scoreboard_2.score(PlayerSide.RIGHT)

                ball.ball_position(GameState.START, player_one, player_two, self.servis , settings,game)

                gf.update_start_screen(screen, settings, player_one, player_two, ball, play_button,restart_button, quit_button,  game,scoreboard_1, scoreboard_2)
            else:


                gf.check_event(player_one, player_two, ball, game,scoreboard_1, scoreboard_2, box_1, box_2, box_3)

                gf.check_score(ball, screen, game, scoreboard_1, scoreboard_2, settings, player_one, player_two)
                gf.box_timer(box_1, box_2, box_3)

                player_one.update_player(settings, PlayerSide.LEFT, game)
                player_two.update_player(settings, PlayerSide.RIGHT, game)

                player_one.update_player_height(settings, PlayerSide.LEFT)
                player_two.update_player_height(settings, PlayerSide.RIGHT)

                gf.check_collision_player(ball, PlayerSide.RIGHT,player_two, player_one,settings)
                gf.check_collision_player(ball, PlayerSide.LEFT,player_two, player_one,settings)
                gf.check_collision_down_up(ball,screen)

                gf.check_suprise(settings, ball, box_1, box_2 , box_3)

                scoreboard_1.score(PlayerSide.LEFT)
                scoreboard_2.score(PlayerSide.RIGHT)

                ball.ball_position(GameState.INGAME, player_one,player_two, self.servis, settings, game)

                gf.update_screen(screen, settings, player_one, player_two, ball,scoreboard_1, scoreboard_2, game, box_1, box_2 , box_3)




game = Game (state = True, servis =PlayerSide.LEFT)
game.start_game()
game.run_game()

