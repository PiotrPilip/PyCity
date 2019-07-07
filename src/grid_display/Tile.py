import pygame

from common.Point import Point
import grid_display.converters as converters


class Tile:
    def __init__(self, pos, size, color=(255, 0, 255)):
        self._pos = pos
        self._size = size
        self._color = color

    def draw(self, screen, camera):
        lx = Point(self._size.x, 0)
        ly = Point(0, self._size.y)
        p0 = converters.flat_to_iso(self._pos).xy
        p1 = converters.flat_to_iso(self._pos + lx).xy
        p2 = converters.flat_to_iso(self._pos + lx + ly).xy
        p3 = converters.flat_to_iso(self._pos + ly).xy
        points = [p0, p1, p2, p3]
        if any([camera.inside(Point(p)) for p in points]):
            points = [camera.translate(Point(p)).xy for p in points]
            pygame.draw.polygon(
                screen,
                self._color,
                points
            )