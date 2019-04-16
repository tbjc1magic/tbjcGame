from utils.Vector import Vector2D
import pygame

class ImageManager(object):
    def __init__(self, fPath, nSubImages=(1,1)):
        

        self.img = pygame.image.load(fPath)
        self.nSubImages = Vector2D(*nSubImages)

        size = Vector2D(*self.img.get_rect().size)
        self.subImageSize = size/nSubImages
        self.imageOrigin = Vector2D(0,0)

    def drawSubImage(self, display, loc, imageIndex=(0,0)):
        
        x,y = [self.imageOrigin[i] + j*self.subImageSize[i] for i,j in enumerate(imageIndex)]
        w,h = self.subImageSize
        display.blit(self.img, loc, (x,y,w,h))


class AnimeElement:
    def __init__(self, display, loc, cycle=1):
        self.__display = display
        self.__imageDict ={}
        self.__lastStatus = None
        self.__lastFrame = None
        self.__loc = loc
        self.__animeClock = -1
        self.__animeCycle = cycle

    def drawFrame(self, loc=None, status=None, frameIndex=None):
        if loc is None: loc = self.__loc

        im = self.__imageDict[status]['imageManager']
        nFrames = self.__imageDict[status]['nFrames']
        shift = self.__imageDict[status]['shift']

        if frameIndex is not None:
            im.drawSubImage(self.display, loc, (frameIndex, shift.y))
            return

        if status != self.__lastStatus:
            self.__lastStatus, self.__lastFrame = status, -1

        self.__animeClock = (self.__animeClock+1)%self.__animeCycle
        delta_frame = 0 if self.__animeClock else 1
        self.__lastFrame = (self.__lastFrame+delta_frame)%nFrames
        im.drawSubImage(self.__display, loc, (self.__lastFrame, shift.y) )
        
    
    def addImage(self, fPath, status=[], nSubImages=Vector2D(1,1)):
        nSubImages = Vector2D(*nSubImages)
        im = ImageManager(fPath, nSubImages)

        for i,s in enumerate(status):
            self.__imageDict[s] = {'shift':Vector2D(0,i),'imageManager':im, 'nFrames': nSubImages.w}


import os
def main():
    pygame.init()
    clock = pygame.time.Clock()

    #DATA_PATH = pkg_resources.resource_filename('data', 'data')
    fPath = os.path.join('data', 'rider_walker.png')

    display = pygame.display.set_mode((300,300))



    ae = AnimeElement(display)
    ae.addImage(fPath, 
                status=['walk_down','walk_left','walk_right','walk_up'],
                nSubImages=(4,4))

    
    run = True
    status = 'walk_down'
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    

        display.fill((0,0,0))


        keys = pygame.key.get_pressed()

        for k,s in [(pygame.K_LEFT, 'walk_left'), 
                    (pygame.K_RIGHT, 'walk_right'),
                    (pygame.K_UP, 'walk_up'),
                    (pygame.K_DOWN, 'walk_down')]:
            if keys[k]: status = s

        ae.drawFrame(status)
        pygame.display.update()

        clock.tick(10)

if __name__ == "__main__":
    main()