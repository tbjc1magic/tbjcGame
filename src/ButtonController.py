import pygame
from utils.Vector import Vector2D

class EventManager:

    def __init__(self):
        self.__childControllerList = []

    def registerController(self, controller):
        self.__childControllerList.append(controller)


    def passEventToChild(self, event):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP]
        
        if event.type in eventTypeAccepted:
            for controller in self.__childControllerList:
                controller.processEvent(event)

class SquareShapeController(EventManager):

    def __init__(self, loc, size):
        EventManager.__init__(self)
        self.__size = Vector2D(*size)
        self.__loc = Vector2D(*loc)

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1  and \
                self.isInside(loc = event.pos) and \
                hasattr(self, 'leftClicked'):
                leftClickMethod = getattr(self, 'leftClicked')
                if callable(leftClickMethod): leftClickMethod()

            if event.button==3 and hasattr(self, 'rightClicked'):
                rightClicked = getattr(self, 'rightClicked')
                if callable(rightClicked): rightClicked()

        if hasattr(event,'pos'):
            event.pos = event.pos - self.__loc
            self.passEventToChild(event)
            event.pos = event.pos + self.__loc
        else:
            self.passEventToChild(event)

    def isInside(self, loc):
        (x,y),(w,h) = self.__loc, self.__size 
        if x<loc[0]<x+w and y<loc[1]<y+h: return True
        return False



class Button(SquareShapeController):

    def __init__(self, top, loc, size):

        self.__loc, self.__size = loc, size
        SquareShapeController.__init__(self, loc, size)
        self.selected = False
        self.top = top

    def draw(self):
        pygame.draw.rect(self.top, (0,0,255), (self.__loc[0], self.__loc[1], self.__size[0], self.__size[1]))


    def leftClicked(self):
        print('leftClick triggered')
        self.selected = True
    
    def rightClicked(self):
        print('rightClick triggered')
        self.selected = False


class _EventManager:

    def __init__(self):
        self.__childControllerList = []

    def registerController(self, controller):
        self.__childControllerList.append(controller)


    def processEvents(self, events):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP]
        
        for event in events:
            if event.type in eventTypeAccepted:
                for controller in self.__childControllerList:
                    controller.processEvent(event)


class RunManager:
    def __init__(self):
        pygame.init()
        self.__eventManager = _EventManager()

    def terminate(self):
        self.runStatus = False

    def run(self):
        
        clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((800,600))

        button = Button(self.__display, (50,50), (100,100))
        self.__eventManager.registerController(button)

        runStatus = True
        while runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    runStatus = False   

            button.draw()
            pygame.display.update()
            self.__eventManager.processEvents(events) 
            clock.tick(10)


import os
def main():
    RunManager().run()

if __name__ == "__main__":
    main()