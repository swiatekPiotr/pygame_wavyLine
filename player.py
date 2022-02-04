import pygame


class Player():

    def __init__(self, game, color, position, dimension):
        self.game = game
        self.color = color
        self.position = position
        self.dimension = dimension

        size = self.game.screen.get_size()


    def move(self):
        pressed = pygame.key.get_pressed()
        # todo create button selection for players
        if pressed[pygame.K_w]:
            self.position += (0, -5)
        if pressed[pygame.K_s]:
            self.position += (0, 5)
        if pressed[pygame.K_a]:
            self.position += (-5, 0)
        if pressed[pygame.K_d]:
            self.position += (5, 0)


    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, pygame.Rect((self.position, self.dimension)))


