from utils.RoundRect import RoundedRect
from utils.Vector import Vector2D
import pygame

def _generateGridPaddedMap(mapSize, nGrid, gridMargin=(3,3), offset=(5,5)):
    
    mapSize, nGrid, gridMargin, offset = map(lambda _:Vector2D(*_),
                                                [mapSize,
                                                 nGrid,
                                                 gridMargin,
                                                 offset])

    gridFullSize = (mapSize-2*offset)//nGrid
    gridContentSize = gridFullSize-2*gridMargin

    #print(gridFullSize*nGrid+2*offset, mapSize)
    #assert gridFullSize*nGrid+2*offset == mapSize, "map can not be fully diveided" 

    gridContent = RoundedRect(gridContentSize, color=(0,0,255), radius=0.1)
    gridSurface = pygame.Surface(gridFullSize)
    gridSurface.blit(gridContent, gridMargin)
    gridMapSurface = pygame.Surface(mapSize)


    #return gridSurface
    for r in range(nGrid[0]):
        for c in range(nGrid[1]):
            loc = gridFullSize*(r,c) + offset
            #if (r,c) == (0,0):
            #print(loc, gridMargin)
            #loc = (0,0)
            gridMapSurface.blit(gridSurface, loc)

    gridMapSurface.set_alpha(100)

    return gridMapSurface

class MapManager():

    def __init__(self, parentSurface, loc, size, nGrid, fPath, gridMargin=(3,3), offset=(2,2)):
        self.parentSurface = parentSurface    
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        img = pygame.image.load(fPath)
        self.backgroundImage = pygame.transform.scale(img, size)
        self.loc = loc

        self.gridMap = _generateGridPaddedMap(size,nGrid, gridMargin=gridMargin, offset=offset)

    def draw(self):
        self.surface.blit(self.backgroundImage, (0,0))
        self.surface.blit(self.gridMap, (0,0))
        self.parentSurface.blit(self.surface, (0,0))


def main():
    pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((800,600))
    
    mm = MapManager(gameDisplay,
                    loc=Vector2D(0,0),
                    size=gameDisplay.get_rect().size, 
                    nGrid=(30,30),
                    gridMargin=(1,1),
                    offset=(1,1),
                    fPath='data/map.JPG'
    )           
                    

    #return
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