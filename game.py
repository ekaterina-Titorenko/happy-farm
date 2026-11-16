import arcade

import settings as cfg
from chicken import Chicken

class FarmWindow(arcade.Window):
    def __init__(self):
        super().__init__(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT, cfg.SCREEN_TITLE)
        self.background_color = cfg.BG_COLOR
        self.chicken = Chicken(cfg.CHICKEN_START_X, cfg.CHICKEN_START_Y)

    def on_draw(self):
        self.clear()
        self.draw_yard()
        self.chicken.draw()


    def draw_yard(self):
        arcade.draw_rect_filled(
            arcade.rect.LRBT(cfg.YARD_LEFT, cfg.YARD_RIGHT,
                             cfg.YARD_BOTTON, cfg.YARD_TOP),
            cfg.YARD_COLOR
        )

    def on_update(self, delta_time):
        self.chicken.update(delta_time)