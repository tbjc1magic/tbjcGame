import pygame


def text_format(message, textSize, textColor):
    newFont=pygame.font.SysFont(None, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def text_cell(msg, width, height, lw, ts, tc):

    canvas = pygame.Surface((width,height), pygame.SRCALPHA)
    canvas.fill((255,255,255))
    pygame.draw.rect(canvas, (100,100,100), (lw,lw,width-2*lw,height-2*lw))

    text = text_format(msg, ts, tc)
    canvas.blit(text,(lw,lw))
    return canvas

from .ButtonController import SquareShapeController
class MenuCell(SquareShapeController):

    def __init__(self, surface, msg, loc, size, widgetID=None, callback=None):
        self.loc = loc
        self.size = size
        self.surface = surface
        self.textCell = text_cell(msg, size[0], size[1], 2, 30, (0,0,0))
        self.widgetID = widgetID
        self.callback=callback
        SquareShapeController.__init__(self, loc, size)

    def draw(self):
        self.surface.blit(self.textCell, self.loc)
 
    def leftClicked(self):
        if self.callback: self.callback()


import functools
class Menu(SquareShapeController):

    def __init__(self, display, items, loc, cellSize, callback=None):
        self.items = items
        self.display = display
        self.cellW, self.cellH = cellSize
        self.canvasSize = (self.cellW, len(items)*self.cellH)
        self.loc = loc
        self.canvas = pygame.Surface(self.canvasSize, pygame.SRCALPHA)
        self.canvas.fill((255,255,255))
        self.menuCells = []

        SquareShapeController.__init__(self, loc, self.canvasSize)

        def cellCallback(cellID):
            event = {'type':'leftClicked',
                     'cellID': cellID}
            if callback: callback(event)

        for idx, text in enumerate(items):
            cell = MenuCell(self.canvas, text, 
                            (0,self.cellH*idx), 
                            cellSize, 
                            widgetID=idx,
                            callback=functools.partial(cellCallback, cellID=idx))
            self.menuCells.append(cell)
            self.registerController(cell)
    

    def draw(self):
        for cell in self.menuCells:
            cell.draw()

        self.display.blit(self.canvas, self.loc)


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

        menu = Menu(self.__display, ['bobo1','bobo2'],(50,50), (100,50))
        self.__eventManager.registerController(menu)

        runStatus = True
        while runStatus:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    runStatus = False   

            menu.draw()
            pygame.display.update()
            self.__eventManager.processEvents(events) 
            clock.tick(5)


import os
def main():
    RunManager().run()

if __name__ == "__main__":
    main()