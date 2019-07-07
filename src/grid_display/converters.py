from common.Point import Point


def iso_to_flat(point):
    return Point((2 * point.y + point.x) / 2, (2 * point.y - point.x) / 2)


def flat_to_iso(point):
    return Point(point.x - point.y, (point.x + point.y) / 2)