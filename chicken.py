import arcade
import settings as cfg


class Chicken:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = cfg.CHICKEN_SPEED

    def update(self, delta_time):
        self.x += self.speed_x * delta_time

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 
                                   cfg.CHICKEN_BODY_WIDTH, cfg.CHICKEN_BODY_HEIGHT, 
                                   cfg.CHICKEN_BODY_COLOR)

        