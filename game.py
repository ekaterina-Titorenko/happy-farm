import arcade


import settings as cfg

class FarmWindow(arcade.Window):
    def __init__(self):
        super().__init__(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT, cfg.SCREEN_TITLE)
        self.background_color = cfg.BG_COLOR

    def on_draw(self):
        self.clear()