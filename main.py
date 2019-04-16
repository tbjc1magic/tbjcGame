

from src.Character import Rider, Infantry
from src.Menu import Menu
import pygame
from utils.Vector import Vector2D
from src.Map import MapManager


from src.RunManager import RunManager




def LeftClicked(obj):
    obj.loc = Vector2D(100,100)
    obj.move([(100,100),(200,100),(300,100),(300,200),(400,200)])

def moveCompleted(obj):
    pass

from src import Constant
class GameManager(RunManager):
    def __init__(self):

        self.cell_size = Constant.cell_size
        super().__init__(self.cell_size*(15,15))

        mm = MapManager(self.display,
                        loc=Vector2D(0,0),
                        size=self.display.get_rect().size, 
                        nGrid=(15,15),
                        gridMargin=(1,1),
                        offset=(1,1),
                        fPath='data/map.JPG')

        self.registerController(mm)

    def setUpGame(self):

        infantry = Infantry(self.display, loc=self.cell_size*2)
        infantry.registerCallBack('leftclick', LeftClicked)
        infantry.registerCallBack('move_complete', moveCompleted)
        rider = Rider(self.display, loc=self.cell_size*(4,3))

        self.registerController(infantry)
        self.registerController(rider)

def main():
    GameManager().run()
  


def main1():

    start = Vector2D(1,1)
    end = Vector2D(4,3)

    import heapq

    w,h = (6,6)
    mem = [[None]*w for _ in range(h)] 

    visited = set([])
    q = []
    heapq.heappush(q, (0,start, None))

    while q:
        cost,cur,p = heapq.heappop(q)
        if cur in visited: continue
        mem[cur[1]][cur[0]] = p
        visited.add(cur)
        for d in [(1,0),(-1,0),(0,1),(0,-1)]:
            nxt = cur+d
            if not 0<=nxt[0]<w or not 0<=nxt[1]<h: continue
            if nxt in visited: continue
            ncost=cost+1
            if p and d != cur-p: ncost+=1
            heapq.heappush(q, (ncost,nxt,cur))

    moves = [end]
    while moves[-1] != start:
        c = moves[-1]
        moves.append(mem[c[1]][c[0]])
    
    print(moves)

if __name__ == "__main__":
    main1()