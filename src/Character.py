from .AnimeElement import AnimeElement
from .ButtonController import SquareShapeController
import pygame
from utils.Vector import Vector2D
class Soldier(AnimeElement, SquareShapeController):   

    def __init__(self, display, loc):
        
        self.loc = loc
        self.display = display
        self.character_size = Vector2D(48,64)
        self.canvasSize = self.subImageSize = (48,64)
        self.canvas = pygame.Surface(self.canvasSize, pygame.SRCALPHA)

        AnimeElement.__init__(self, self.canvas, Vector2D(0,0))
        SquareShapeController.__init__(self, loc, self.subImageSize)
        

        fPath = os.path.join('data', 'rider_walker.png')
        self.addImage(fPath, 
                      status=['walk_down','walk_left','walk_right','walk_up'], 
                      nSubImages=Vector2D(4,4))


    def draw(self):
        self.canvas.fill((0,0,0))
        self.drawFrame(None,'walk_right')
        self.display.blit(self.canvas, self.loc)


    def leftClicked(self):
        print('here?')

    def rightClicked(self):
        print('right clicked')


from .ButtonController import EventManager


class RunManager:
    def __init__(self):
        pygame.init()
        self.__eventManager = EventManager()

    def terminate(self):
        self.runStatus = False

    def run(self):
        
        clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((800,600))

        soldier = Soldier(self.__display, (100,100))
        self.__eventManager.registerController(soldier)

        runStatus = True
        while runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    runStatus = False   

            soldier.draw()
            pygame.display.update()
            self.__eventManager.processEvents(events) 
            clock.tick(5)


import os
def main():
    RunManager().run()


if __name__ == "__main__":
    main()