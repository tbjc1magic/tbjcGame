import pygame
from src.ButtonController import  EventManager
from src.AnimeManager import AnimeManager
import abc



class RunManager:

    def __init__(self, size):
        pygame.init()
        self.display = pygame.display.set_mode(size)
        self.eventManager = EventManager()
        self.animeManager = AnimeManager(self.display)
        self.runStatus = True

    def terminate(self):
        self.runStatus = False

    def processEvents(self, events):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP,
                             pygame.MOUSEMOTION]
        
        for event in events:
            if event.type in eventTypeAccepted:
                self.eventManager.passEventToChild(event)

    def registerController(self, controller, priority=-1):
        self.eventManager.registerController(controller)
        self.animeManager.registerController(controller, priority)

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