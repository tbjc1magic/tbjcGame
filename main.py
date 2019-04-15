

from src.Character import Rider, Infantry
from src.Menu import Menu
import pygame
from utils.Vector import Vector2D
from src.Map import MapManager


from src.RunManager import RunManager




def LeftClicked(obj):
    obj.loc = Vector2D(100,100)
    obj.move([(100,100),(200,100),(300,100),(300,200),(400,200)])
    print('am I here?')

def moveCompleted(obj):
    print('move completed')

class GameManager(RunManager):
    def __init__(self):
        self.display = pygame.display.set_mode((48*15,64*15))
        super().__init__()

    def setUpGame(self):

        mm = MapManager(self.display,
                        loc=Vector2D(0,0),
                        size=self.display.get_rect().size, 
                        nGrid=(15,15),
                        gridMargin=(1,1),
                        offset=(1,1),
                        fPath='data/map.JPG'
        )    

        self.registerController(mm)

        infantry = Infantry(self.display, (48*2,64*2))
        infantry.registerCallBack('leftclick', LeftClicked)
        infantry.registerCallBack('move_complete', LeftClicked)
        #infantry.move([(100,100),(200,100),(300,100),(300,200),(400,200)])
        rider = Rider(self.display, (48*2,64*4))

        self.registerController(infantry)
        self.registerController(rider)

def main():
    GameManager().run()
  

if __name__ == "__main__":
    main()