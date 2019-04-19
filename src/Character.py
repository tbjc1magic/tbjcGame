from .AnimeElement import AnimeElement
from .ButtonController import SquareShapeController
import pygame
from utils.Vector import Vector2D
from src import Constant
class Soldier(AnimeElement, SquareShapeController):   

    def __init__(self, display, loc, fPath):
        
        self.__display = display
        self.__character_size = Constant.cell_size
        self.__canvasSize = self.__subImageSize = Constant.cell_size
        self.__canvas = pygame.Surface(self.__canvasSize, pygame.SRCALPHA, 32)
        self.__showMenus = False

        AnimeElement.__init__(self, self.__canvas, Vector2D(0,0), 
                            Constant.character_refresh_cycle)
        SquareShapeController.__init__(self, loc, self.__subImageSize)
        
        self.addImage(fPath, 
                      status=['walk_down','walk_left','walk_right','walk_up'], 
                      nSubImages=Vector2D(4,4))

        self.__status = 'walk_down'
        self.__moves = []



    def move(self, route):
        speed = Constant.character_move_speed
        moves = [(None,self.loc)]
        status_dict = {(1,0):'walk_right', (-1,0):'walk_left', 
                       (0,1):'walk_down',  (0,-1):'walk_up'}

        for pos in route[1:]:
            diff = pos - moves[-1][1]
            
            if abs(diff[0]) and abs(diff[1]): 
                raise Exception('charecter can only move along X/Y direcion')

            dist = abs(diff[0])+abs(diff[1])
            dire = diff//dist
            nFrames = int(dist//speed)
            
            for _ in range(nFrames): 
                nxt_status = (status_dict[dire], dire*speed+moves[-1][1])
                moves.append(nxt_status)
        self.__moves = moves[1:]

    def draw(self):


        if self.__moves:
            isMove = True
            self.__status, self.loc = self.__moves.pop(0)
        else:
            isMove = False

        self.__canvas.fill((0,0,0,0))
        self.drawFrame(None,self.__status)
        self.__display.blit(self.__canvas, self.loc)
        
        if isMove and len(self.__moves)==0 and 'move_complete' in self.__callbacks:
            self.__callbacks['move_complete'](self)

        return len(self.__moves)>0
        

    def leftClicked(self):
        if 'left_click' in self.__callbacks:
            self.__callbacks['left_click'](self)


    def rightClicked(self):
        pass


class Rider(Soldier):
    def __init__(self, display, loc):
        fPath = 'data/rider_walk.png'
        Soldier.__init__(self, display, loc, fPath)

class Infantry(Soldier):
    def __init__(self, display, loc):
        fPath = 'data/infantry_walk.png'
        Soldier.__init__(self, display, loc, fPath)


from .ButtonController import _EventManager


class RunManager:
    def __init__(self):
        pygame.init()
        self.__eventManager = _EventManager()

    def terminate(self):
        self.runStatus = False

    def run(self):
        
        clock = pygame.time.Clock()
        self.__display = pygame.display.set_mode((800,600))

        soldier = Soldier(self.__display, (100,100), 'data/infantry_walk.png')
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