from util import RoundedRect
import pygame

def _add_grids(surface, gridSize, gridCornerRadius, gridColor, margin, offset):
    pass



class MapManager():

    def __init__(self, parentSurface, loc, size):
        self.parentSurface = parentSurface    
        self.surface = pygame.surface(size, pygame.SRCALPHA)
        
    def draw(self):
        self.surface.blit()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((800,600))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        gameDisplay.fill((0,0,0))
        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    quit()