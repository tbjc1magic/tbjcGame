

from src.Character import Rider, Infantry
from src.ButtonController import _EventManager, EventManager
from src.Menu import Menu
import pygame
from utils.Vector import Vector2D
from src.Map import MapManager


class RunManager(EventManager):
    def __init__(self):
        pygame.init()
        EventManager.__init__(self)

    def terminate(self):
        self.runStatus = False

    def processEvents(self, events):

        eventTypeAccepted = [pygame.MOUSEBUTTONDOWN, 
                             pygame.MOUSEBUTTONUP]
        
        for event in events:
            if event.type in eventTypeAccepted:
                self.passEventToChild(event)

    def run(self):
        
        clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((800,600))
        menu = Menu(self.__display, ['attack','defend'], (250,50), (100,25))
        infantry = Infantry(self.__display, (100,100))
        infantry.move([(100,100),(200,100),(300,100),(300,200),(400,200)])
        rider = Rider(self.__display, (100,200))




        self.registerController(infantry)
        self.registerController(rider)
        self.registerController(menu)

        moves = []
        x,y = 100,100
        for i in range(30):
            y +=5
            moves.append(('walk_down',Vector2D(x,y)))

        for j in range(30):
            x +=5
            moves.append(('walk_right', Vector2D(x,y)))

        flag = False 
        flag1 = False
        i = 0
        runStatus = True
        while runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    runStatus = False   

            self.__display.fill((0,0,0))



            #status, loc = moves[i]
            #soldier.status, soldier.loc = status, loc
            #i = (i+1)%len(moves)
            #i = min(i+1, len(moves)-1)
            menu.draw()
            if not infantry.draw():
                flag = True
            
            if flag and not flag1:
                rider.move([(100,200),(200,200),(300,200),(300,300),(400,300)])
                flag1 = True

            rider.draw()
            pygame.display.update()
            self.processEvents(events) 

            clock.tick(10)


import os
def main():
    RunManager().run()


if __name__ == "__main__":
    main()