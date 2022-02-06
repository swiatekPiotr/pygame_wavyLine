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
            self.position[1] -= 0.1
        if pressed[pygame.K_s]:
            self.position[1] += 0.1
        if pressed[pygame.K_a]:
            self.position[0] -= 0.1
        if pressed[pygame.K_d]:
            self.position[0] += 0.1


    def draw(self):
        pygame.draw.rect(self.game.screen, self.color,
                         pygame.Rect(self.position[0], self.position[1], self.dimension[0], self.dimension[1]))


