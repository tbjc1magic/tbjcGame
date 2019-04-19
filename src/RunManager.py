import pygame
from src.ButtonController import  EventManager
from src.AnimeManager import AnimeManager
from src.ButtonController import SquareShapeController
import abc
from utils.Vector import Vector2D


class RunManager(SquareShapeController):

    def __init__(self, size):
        SquareShapeController.__init__(self, Vector2D(0,0), size)
        pygame.init()
        self.display = pygame.display.set_mode(size)
        self.eventManager = EventManager()
        self.animeManager = AnimeManager(self.display)
        self.runStatus = True

        self.eventManager.registerController(self)

    def terminate(self):
        self.runStatus = False

    def processEvents(self, events):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP,
                             pygame.MOUSEMOTION]
        
        for event in events:
            if event.type in eventTypeAccepted:
                self.eventManager.passEventToChild(event)

    def registerController(self, controller, animePriority=-1, eventPriority=-1):
        self.eventManager.registerController(controller, eventPriority)
        self.animeManager.registerController(controller, animePriority)

    @abc.abstractclassmethod
    def setUpGame(self):
        return

    def run(self):

        self.setUpGame()

        clock = pygame.time.Clock()
 
        while self.runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.runStatus = False   

            
            self.processEvents(events) 
            self.animeManager.draw()
            pygame.display.update()
            clock.tick(60)

def main():

    GameManager().run()

if __name__ == "__main__":
    main()