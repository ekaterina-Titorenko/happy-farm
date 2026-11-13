import arcade
import settings as cfg


class Chicken:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 
                                   cfg.CHICKEN_BODY_WIDTH, cfg.CHICKEN_BODY_HEIGHT, 
                                   cfg.CHICKEN_BODY_COLOR)

        