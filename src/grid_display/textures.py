import random
PWD = r"..\..\resources\textures\grass_1.png"

import pygame

SIZE = 800, 600


class Texture:
    def __init__(self, image_pwd=PWD):
        self.image = pygame.image.load(image_pwd)


    def render(self, screen, polygon, pos):
        max_w = max(x[0] for x in polygon)
        max_h = max(x[1] for x in polygon)
        surf = pygame.Surface((max_w, max_h), depth=32)
        surf.blit(self.image, (0,0))
        surf.convert_alpha()
        target = pygame.surfarray.pixels_alpha(surf)
        target[:] = pygame.surfarray.array2d(surf)
        mask = pygame.Surface((max_w, max_h))
        pygame.draw.polygon(mask, 255, polygon)
        screen.blit(apply_alpha(self.image, mask), pos)


def tile_texture(texture, size):
    result = pygame.Surface(size, depth=32)
    for x in range(0, size[0], texture.get_width()):
        for y in range(0, size[1], texture.get_height()):
            result.blit(texture, (x, y))
    return result


def apply_alpha(texture, mask):
    """
    Image should be  a 24 or 32bit image,
    mask should be an 8 bit image with the alpha
    channel to be applied
    """
    texture = texture.convert_alpha()
    target = pygame.surfarray.pixels_alpha(texture)
    target[:] = pygame.surfarray.array2d(mask)
    # surfarray objets usually lock the Surface.
    # it is a good idea to dispose of them explicitly
    # as soon as the work is done.
    del target
    return texture


def stamp(image, texture, mask):
    image.blit(apply_alpha(texture, mask), (15, 15))




def main():
    screen = pygame.display.set_mode(SIZE)
    screen.fill((255,255,255))
    texture = tile_texture(pygame.image.load(r"..\..\resources\textures\grass_1.png"), SIZE)
    mask = pygame.Surface(SIZE,)
    # Create sample mask:
    polygon = [[0, 0], [25, 0], [25, 25], [0, 25]]
    t = Texture()
    #pygame.draw.polygon(mask, 255,
    #                    [[0, 0], [25, 0], [25, 25], [0, 25]], 0)

    #stamp(screen, texture, mask)
    t.render(screen, polygon, (50,50))
    pygame.display.flip()
    while not any(pygame.key.get_pressed()):
        pygame.event.pump()
        pygame.time.delay(30)


if __name__ == "__main__":
    pygame.init()
    try:
        main()
    finally:
        pygame.quit()