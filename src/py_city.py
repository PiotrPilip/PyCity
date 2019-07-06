import pygame

from gamestates.menu_state import MenuState
import constants

import configparser


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(constants.CONFIG_FILE)
    w = int(config[constants.C_WINDOW][constants.C_WIDTH])
    h = int(config[constants.C_WINDOW][constants.C_HEIGHT])

    flags = 0
    flags |= pygame.FULLSCREEN if config[constants.C_WINDOW][constants.C_FULLSCREEN] == "1" else 0

    window = pygame.display.set_mode((w, h), flags)

    gamestates = list()
    gamestates.append(MenuState())

    while True:
        state = gamestates[-1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            state.handle_events(event)

        state.render(window)
        pygame.display.flip()
