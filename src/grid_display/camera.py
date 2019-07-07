from common.Point import Point
import grid_display.converters as conv


class Camera:
    def __init__(self, view_window, start=Point(0, 0)):
        self._pos = start
        self._view_window = view_window

    def translate(self, point):
        return self._pos + point

    def inside(self, point):
        x = Point(self._view_window[0], 0)
        y = Point(0, self._view_window[1])
        translated = conv.iso_to_flat(self.translate(point))
        print(self._pos.x)

        if self._pos.x < translated.x < (self._pos + x).x and self._pos.y < translated.y < (self._pos + y).y:
            return True
        else:
            return False

    def move(self, p):
        self._pos = self._pos + p
