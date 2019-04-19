

from src.Character import Rider, Infantry
from src.Menu import Menu
import pygame
from utils.Vector import Vector2D
from src.Map import MapManager
from src.RunManager import RunManager




def leftClicked(obj, host):
    #obj.loc = Vector2D(100,100)
    #obj.move([(100,100),(200,100),(300,100),(300,200),(400,200)])
    #import ipdb; ipdb.set_trace()
    print(obj)


def moveCompleted(obj, host):
    pass

def rightClicked(obj, host):
    print(obj)

import functools
from src import Constant
class GameManager(RunManager):
    def __init__(self):

        self.gridSize = Constant.cell_size
        super().__init__(self.gridSize*(15,15))

        self.mapManager = MapManager(self.display,
                                    loc=Vector2D(0,0),
                                    size=self.display.get_rect().size, 
                                    nGrid=(15,15),
                                    gridMargin=(1,1),
                                    offset=(1,1),
                                    fPath='data/map.JPG')

        self.registerController(self.mapManager, animePriority=-100, 
                                eventPriority=-100)
        callback = functools.partial(leftClicked, host=self)
        self.mapManager.registerCallBack('left_click', callback)


    def initializeCharacter(self, cls, chess_pos):
        character = cls(self.display, loc=chess_pos*self.gridSize)

        callback = functools.partial(leftClicked, host=self)
        character.registerCallBack('left_click', callback)

        callback = functools.partial(moveCompleted, host=self)
        character.registerCallBack('move_complete', callback)
        self.registerController(character)

        self.mapManager.markOccupied(chess_pos)
        return character

    def moveCharacter(self, character, destination):
        start = self.mapManager.getChessPosition(character.loc)
        route = self.mapManager.generateMoves(start, destination)
        character.move(route)

    def setUpGame(self):
        callback = functools.partial(rightClicked, host=self)
        self.registerCallBack('right_click', callback)
        infantry = self.initializeCharacter(Infantry, Vector2D(2,2))
        rider = self.initializeCharacter(Rider, Vector2D(3,3))
        #import ipdb; ipdb.set_trace()
        #self.moveCharacter(infantry, (5,5))

def main():
    GameManager().run()
  


if __name__ == "__main__":
    main()