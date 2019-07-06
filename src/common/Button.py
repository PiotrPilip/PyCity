import pygame
pygame.init()

from common.Point import Point
import constants

class Button:
    def __init__(self, pos: Point, size: Point, action, text):
        self._pos = pos
        self._size = size
        self._color = 255, 0, 0
        self._action = action
        self._font = pygame.font.SysFont("Arial", 40)
        self._text = self._font.render(text, True, (0, 0, 0))

    def render(self, screen):
        pygame.draw.rect(
            screen,
            self._color,
            [self._pos.xy, self._size.xy]
            )
        x = self._pos.x + self._size.x // 2 - self._text.get_width() // 2
        y = self._pos.y + self._size.y // 2 - self._text.get_height() // 2
        screen.blit(self._text, (x, y))

    def clicked(self, pos: Point):
        end = self._pos + self._size
        if self._pos.x < pos.x < end.x and self._pos.y < pos.y < end.y:
            self._action()