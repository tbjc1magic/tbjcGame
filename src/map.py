from utils.RoundRect import RoundedRect
from utils.Vector import Vector2D
import pygame


def _generateGridPaddedMap(mapSize, nGrid, margin=0.05):
    
    gridSize = Vector2D(*mapSize)/nGrid
    print(gridSize)

class MapManager():

    def __init__(self, parentSurface, loc, size, nGrid, fPath, margin=0.05, offset=0):
        self.parentSurface = parentSurface    
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        img = pygame.image.load(fPath)
        self.backgroundImage = pygame.transform.scale(img, size)
        self.loc = loc

        _generateGridPaddedMap(size,nGrid, margin)



        #gridSize = 
        #for r in range(nGrid[0]):
        #    for c in range(nGrid[1]):
                


    def draw(self):
        self.surface.blit(self.backgroundImage, (0,0))
        self.parentSurface.blit(self.surface, (0,0))


def main():
    pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((800,600))
    
    mm = MapManager(gameDisplay,
                    loc=Vector2D(0,0),
                    size=gameDisplay.get_rect().size, 
                    nGrid=(10,10),
                    fPath='data/map.JPG'
    )           
                    

    return
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        gameDisplay.fill((0,0,0))
        mm.draw()
        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()