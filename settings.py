import pygame


class Settings():

    def __init__(self):
        # Display settings
        self.screen_width = 1200
        self.screen_height = 700
        self.rgb_color = (160, 250, 110)

        #P layers settings
        self.playerleft_width = 30
        self.playerleft_height = 200
        self.playerright_width = 30
        self.playerright_height = 200
        self.player_color = (0, 0, 0)
        self.playerleft_speed = 2
        self.playerright_speed = 2

        # Ball settings
        self.ball_speed = 2
        self.ball_radius = 20
        self.ball_color = 60, 60, 60
        self.ball_limit = 1


        #Score
        self.stats_right = 0
        self.stat_left = 0


    def update_speed(self):
        self.ball_speed += 0.05










