import pygame
from ball import PlayerSide


class ScoreBoard():

    def __init__(self, screen , settings, side):
        if side == PlayerSide.LEFT:
            self.stats_left = 5
        elif side == PlayerSide.RIGHT:
            self.stats_right = 5

        self.settings = settings
        self.color = settings.rgb_color
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (30, 30 ,30)
        self.font = pygame.font.SysFont(None, 48)

    def score(self,  side ):
        if side == PlayerSide.LEFT:
            score_str_left = str(self.stats_left)
            self.score_image_left = self.font.render(score_str_left, True, self.text_color, self.color)
            self.score_rect_left = self.score_image_left.get_rect()
            self.score_rect_left.centery = self.screen_rect.centery
            self.score_rect_left.centerx = self.screen_rect.centerx - 100

        elif side == PlayerSide.RIGHT:
            score_str_right = str(self.stats_right)
            self.score_image_right = self.font.render(score_str_right, True, self.text_color, self.color)
            self.score_rect_right = self.score_image_right.get_rect()
            self.score_rect_right.centery = self.screen_rect.centery
            self.score_rect_right.centerx = self.screen_rect.centerx + 100

    def draw_score(self, side):
        if side == PlayerSide.LEFT:
            self.screen.blit(self.score_image_left, self.score_rect_left)
        if side == PlayerSide.RIGHT:
            self.screen.blit(self.score_image_right, self.score_rect_right)


