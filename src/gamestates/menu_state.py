import pygame

from gamestates.i_gamestate import IGameState
from common.Button import Button
from common.Point import Point
import constants


import configparser

BACKGROUND_COLOR = 0, 0, 0


class MenuState(IGameState):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(constants.CONFIG_FILE)

        w = int(config[constants.C_WINDOW][constants.C_WIDTH])
        h = int(config[constants.C_WINDOW][constants.C_HEIGHT])
        middle = w // 2
        x_l = middle - w // 4
        x_p = middle + w // 4
        ys = [y for y in range(h // 16, h, h//4)]
        self._buttons = [
            Button(Point(x_l, ys[0]), Point(x_p - x_l, h//6), lambda: print("button 1"), "Start New Game"),
            Button(Point(x_l, ys[1]), Point(x_p - x_l, h//6), lambda: print("button 2"), "Load Game"),
            Button(Point(x_l, ys[2]), Point(x_p - x_l, h//6), lambda: print("button 3"), "Options"),
            Button(Point(x_l, ys[3]), Point(x_p - x_l, h//6), lambda: exit(), "Exit"),
        ]

    def render(self, screen):
        screen.fill(BACKGROUND_COLOR)
        for button in self._buttons:
            button.render(screen)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in self._buttons:
                    button.clicked(Point(event.pos))

