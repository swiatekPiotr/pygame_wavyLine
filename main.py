import pygame, sys
from player import Player


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 600))

        pygame.display.set_caption("Wavy Lines")

        self.player1 = Player(self, (255, 100, 100), [200, 200], [5, 5])
        self.player2 = Player(self, (100, 255, 100), [800, 400], [5, 5])
        # todo create random numbers of colors and position

        clock = pygame.time.Clock()
        while True:
            clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.draw()
            self.move()
            pygame.display.flip()
            pygame.display.update()

    def draw(self):
        self.player1.draw()
        self.player2.draw()


    def move(self):
        self.player1.move()
        self.player2.move()


if __name__ == "__main__":
    Game()