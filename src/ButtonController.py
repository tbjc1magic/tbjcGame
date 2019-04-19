import pygame
from utils.Vector import Vector2D

class EventManager:

    def __init__(self, firstReact=True, passToChildren=True):
        self.__childControllerList = []
        self.__callbacks = {}
        self.__firstReact = firstReact
        self.__passToChildren = passToChildren

    def registerController(self, controller, priority=-1):

        self.__childControllerList.append((-priority, controller))
        self.__childControllerList = sorted(self.__childControllerList, 
                                            key=lambda _:_[0])

    def registerCallBack(self, key, func):
        self.__callbacks[key] = func


    def passEventToChild(self, event):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP,
                             pygame.MOUSEMOTION]
        response = False
        if event.type in eventTypeAccepted:
            for _, controller in self.__childControllerList:
                childResponse = controller.processEvent(event)
                if self.__firstReact and childResponse: return True
                response = childResponse or response
        
        return response

    def processEvent(self, event):

        if not self.isInside(loc = event.pos): return

        response = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 'left_click' in self.__callbacks:
                    self.__callbacks['left_click'](self)
                    response = True

            if event.button == 3: 
                if 'right_click' in self.__callbacks:
                    self.__callbacks['right_click'](self)
                    response = True

        if event.type == pygame.MOUSEMOTION:
            if 'hover' in self.__callbacks:
                self.__callbacks['hover'](pygame.mouse.get_pos())
                response = True
        
        if not self.__passToChildren: return response

        childResponse = False
        if hasattr(event,'pos'):
            event.pos = event.pos - self.loc
            childResponse = self.passEventToChild(event)
            event.pos = event.pos + self.loc
        else:
            childResponse = self.passEventToChild(event)

        return response or childResponse

        

class SquareShapeController(EventManager):

    def __init__(self, loc, size):
        EventManager.__init__(self)
        self.size = Vector2D(*size)
        self.loc = Vector2D(*loc)
        

    def isInside(self, loc):
        (x,y),(w,h) = self.loc, self.size 
        if x<loc[0]<x+w and y<loc[1]<y+h: return True
        return False



class Button(SquareShapeController):

    def __init__(self, top, loc, size):

        #self.__loc, self.__size = loc, size
        SquareShapeController.__init__(self, loc, size)
        self.selected = False
        self.top = top

    def draw(self):
        pygame.draw.rect(self.top, (0,0,255), (self.loc[0], self.loc[1], self.size[0], self.size[1]))

    


class _EventManager:

    def __init__(self):
        self.__childControllerList = []

    def registerController(self, controller):
        self.__childControllerList.append(controller)


    def processEvents(self, events):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP,
                             pygame.MOUSEMOTION]
        
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