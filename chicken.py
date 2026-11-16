from math import hypot
from random import uniform

import arcade
import settings as cfg


class Chicken:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = cfg.CHICKEN_SPEED
        self.target_x = x
        self.target_y = y
        self.rest_remaining = cfg.INITIAL_TIME
        self.choose_target()

    def choose_target(self):
        """Выбираем точку внутри двора с запасом для размеров птицы."""
        margin_x = cfg.CHICKEN_BODY_WIDTH / cfg.HALF_DIVISOR + cfg.CHICKEN_EDGE_MARGIN
        margin_y = cfg.CHICKEN_BODY_HEIGHT / cfg.HALF_DIVISOR + cfg.CHICKEN_EDGE_MARGIN
        for _ in range(cfg.CHICKEN_TARGET_ATTEMPTS):
            self.target_x = uniform(cfg.YARD_LEFT + margin_x, cfg.YARD_RIGHT - margin_x)
            self.target_y = uniform(cfg.YARD_BOTTON + margin_y, cfg.YARD_TOP - margin_y)
            if hypot(self.target_x - self.x, self.target_y - self.y) >= cfg.CHICKEN_MIN_TRIP:
                break

    def update(self, delta_time):
        if self.rest_remaining > cfg.INITIAL_TIME:
            self.rest_remaining = max(cfg.INITIAL_TIME, self.rest_remaining - delta_time)
            return
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = hypot(dx, dy)
        step = self.speed * delta_time
        if distance <= step:
            self.x = self.target_x
            self.y = self.target_y
            self.rest_remaining = uniform(cfg.CHICKEN_REST_MIN, cfg.CHICKEN_REST_MAX)
            self.choose_target()
            return
        self.x += dx / distance * step
        self.y += dy / distance * step

    def draw(self):
        arcade.draw_ellipse_filled(
            self.x, self.y,
            cfg.CHICKEN_BODY_WIDTH, cfg.CHICKEN_BODY_HEIGHT,
            cfg.CHICKEN_BODY_COLOR,
        )
