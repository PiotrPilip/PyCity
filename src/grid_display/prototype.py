import pygame

from grid_display.Tile import Tile
from grid_display.camera import Camera
from common.Point import Point

window = pygame.display.set_mode((600, 600))
tiles = [
    Tile(Point(60 + i*50, 60 + j*50), Point(50, 50), color=(255, 0, 255) if (i+j*j) % 2 ==0 else (0, 255, 0))
    for i in range(8) for j in range(8)
]

c = Camera((600, 600))

while True:
    for event in pygame.event.get():
        window.fill((0, 0, 0))
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            move = Point(0,0)
            if event.key == pygame.K_LEFT:
                move = move + Point(1, 0)
            if event.key == pygame.K_RIGHT:
                move = move + Point(-1, 0)
            c.move(move)
        for t in tiles:
            t.draw(window, c)
        pygame.display.flip()
