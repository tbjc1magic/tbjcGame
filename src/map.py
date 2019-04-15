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

def _generateGridPaddedMap(mapSize, nGrid, omit=[]):
    
    mapSize, nGrid = Vector2D(*mapSize), Vector2D(*nGrid)
    gridFullSize = mapSize//nGrid
    #import ipdb; ipdb.set_trace()

    gridMapSurface = pygame.Surface(mapSize, pygame.SRCALPHA, 32)
    gridSurface = pygame.Surface(gridFullSize, pygame.SRCALPHA, 32)
    gridSurface.fill((0,0,255,100))

    for r in range(nGrid[0]):
        for c in range(nGrid[1]):
            loc = gridFullSize*(r,c)
            
            gridMapSurface.blit(gridSurface, loc)

    return gridMapSurface


class MapManager():

    def __init__(self, parentSurface, loc, size, nGrid, fPath, gridMargin=(3,3), offset=(2,2)):
        self.parentSurface = parentSurface    
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        img = pygame.image.load(fPath)
        self.size = Vector2D(*size)
        self.backgroundImage = pygame.transform.scale(img, size)
        self.loc = loc
        self.gridSize = Vector2D(*size)/nGrid
        #self.fog = _generateGridPaddedMap(size,nGrid, omit=[])
        self.fog = None
        self.nGrid = nGrid
        self.cursor_pos = None

    def draw(self):
        #self.surface.blit(self.backgroundImage, (0,0))
        self.surface.fill((0,0,0))
        if self.fog: self.surface.blit(self.fog, (0,0))
        
        self.parentSurface.blit(self.surface, (0,0))

        if self.cursor_pos:
            left_top = self.cursor_pos*self.gridSize
            pygame.draw.rect(self.parentSurface,(255,255,255),(*left_top, *self.gridSize),3)




    def processEvent(self, event):

        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            self.cursor_pos = Vector2D(*mouse_position)//self.gridSize
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                w,h = self.size
                self.fog = _generateGridPaddedMap(self.size,self.nGrid, omit=[])

            if event.button == 3:
                self.fog = None

from .ButtonController import _EventManager

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
                    
    mm.getChessPosition(Vector2D(90,80))
    mm.draw()
    pygame.display.update()
    while pygame.event.wait().type != pygame.QUIT: pass

class RunManager:
    def __init__(self):
        pygame.init()
        self.__eventManager = _EventManager()

    def terminate(self):
        self.runStatus = False

    def run(self):
        
        clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((800,600))

        
        mm = MapManager(self.__display,
                        loc=Vector2D(0,0),
                        size=self.__display.get_rect().size, 
                        nGrid=(40,30),
                        gridMargin=(1,1),
                        offset=(1,1),
                        fPath='data/map.JPG'
        )            
        self.__eventManager.registerController(mm)                
        #mm.getChessPosition(Vector2D(90,80))

        runStatus = True
        while runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    runStatus = False   

            mm.draw()
            pygame.display.update()
            self.__eventManager.processEvents(events) 
            clock.tick(120)


import os
def main():
    RunManager().run()


if __name__ == "__main__":
    main()