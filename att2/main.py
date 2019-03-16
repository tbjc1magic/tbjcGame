import pygame
import pkg_resources
import os
import sys

from util import Vector



class ImageManager(object):
    def __init__(self, fPath, display, nSubImages=Vector((1,1))):
        

        self.img = pygame.image.load(fPath)
        self.nSubImages = Vector(nSubImages)

        size = Vector(self.img.get_rect().size)

        self.display = display
        self.subImageSize = size/nSubImages
        self.imageOrigin = Vector((0,0))
        print(size, nSubImages, self.subImageSize)


    def drawSubImage(self, loc, imageIndex=(0,0)):
        
        x,y = [self.imageOrigin[i] + j*self.subImageSize[i] for i,j in enumerate(imageIndex)]
        w,h = self.subImageSize
        self.display.blit(self.img, loc, (x,y,w,h))



class Character(ImageManager):

    def __init__(self,  fPath='', display=None, nSubImages=(1,1)):
        
        super(Character, self).__init__(fPath, display, nSubImages)

        self.lastStatus = 0  ## (0,0) means standing
        self.animeCounter = 0
        self.position = Vector((100,100))
        self.velocity = Vector((5,5))
        self.direction2RowMap = {Vector((0,1)):0, Vector((0,-1)):3, Vector((1,0)):2, Vector((-1,0)):1}

    def move(self, direction):
        status = self.direction2RowMap[direction]
        if self.lastStatus != status:
            self.lastStatus = status
            self.animeCounter = 0

        self.position = self.position + self.velocity * direction


    def draw(self):
        self.drawSubImage(self.position, (self.animeCounter, self.lastStatus))
        self.animeCounter = (self.animeCounter+1)%4



class AnimeManager(object):
    def __init__(self):
        pygame.init()

        DATA_PATH = pkg_resources.resource_filename(__name__, 'data')
        fPath = os.path.join(DATA_PATH, 'rider_walker.png')

        self.display = pygame.display.set_mode((800,600))
        self.c = 0
        self.soldier = Character(fPath=fPath, display=self.display, nSubImages=(4,4))


    def draw(self):
        
        
        self.display.fill((0,0,0))

        self.soldier.draw()

        pygame.draw.rect(self.display, 
                            (255,0,0),
                            (100,100,48,64),
                            1
                        )
        pygame.display.update()
        self.c = (self.c+1)%4

    def run(self):


        clock = pygame.time.Clock()
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False    

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.soldier.move((-1,0))

            if keys[pygame.K_RIGHT]:
                self.soldier.move((1,0))

            if keys[pygame.K_UP]:
                self.soldier.move((0,-1))

            if keys[pygame.K_DOWN]:
                self.soldier.move((0,1))


            self.draw()
            clock.tick(7)

def main():



    animeManager = AnimeManager()
    animeManager.run()

def main1():
    print(Vector((192,256))/(4,4))
    print 123

if __name__ == "__main__":
    main()