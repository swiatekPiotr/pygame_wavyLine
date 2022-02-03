import pygame, sys
from player import Player


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 600))

        pygame.display.set_caption("Wavy Lines")

        self.player = Player((255, 100, 100), (200, 200))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)


if __name__ == "__main__":
    Game()