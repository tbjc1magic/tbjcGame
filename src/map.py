from utils.RoundRect import RoundedRect
from utils.Vector import Vector2D
import pygame

def _generateFancyGridPaddedMap(mapSize, nGrid, gridMargin=(3,3), offset=(5,5)):
    
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

            gridMapSurface.blit(gridSurface, loc)

    gridMapSurface.set_alpha(100)

    return gridMapSurface

def _generateGridPaddedMap(mapSize, nGrid):
    
    mapSize, nGrid = Vector2D(*mapSize), Vector2D(*nGrid)
    gridFullSize = mapSize//nGrid
    #import ipdb; ipdb.set_trace()

    gridMapSurface = pygame.Surface(mapSize, pygame.SRCALPHA, 32)
    gridSurface = pygame.Surface(gridFullSize, pygame.SRCALPHA, 32)
    gridSurface.fill((0,0,255,100))

    for r in range(nGrid[0]):
        for c in range(nGrid[1]):
            loc = gridFullSize*(r,c)
            if abs(r-10) + abs(c-10)<4: continue
            
            gridMapSurface.blit(gridSurface, loc)

    return gridMapSurface


class MapManager():

    def __init__(self, parentSurface, loc, size, nGrid, fPath, gridMargin=(3,3), offset=(2,2)):
        self.parentSurface = parentSurface    
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        img = pygame.image.load(fPath)
        self.backgroundImage = pygame.transform.scale(img, size)
        self.__loc = loc

        self.gridMap = _generateGridPaddedMap(size,nGrid)

    def draw(self):
        self.surface.blit(self.backgroundImage, (0,0))
        self.surface.blit(self.gridMap, (0,0))
        self.parentSurface.blit(self.surface, (0,0))





def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    
    mm = MapManager(gameDisplay,
                    loc=Vector2D(0,0),
                    size=gameDisplay.get_rect().size, 
                    nGrid=(40,30),
                    gridMargin=(1,1),
                    offset=(1,1),
                    fPath='data/map.JPG'
    )            
                    
    mm.draw()
    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT: pass

if __name__ == "__main__":
    main()