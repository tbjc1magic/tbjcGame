import pygame
import pkg_resources
import os
import sys

from util import Vector, RoundedRect


class MapManager():
    def __init__(self, loc, size, gridSize, lineWidth=1):
        


    def draw(self):

        nrow, ncol = size[0]/gridSize[0], size[1]/gridSize[1]

        for ix in range(ncol):
            for iy in range(nrow):
                x,y = ix*gridSize[0], iy*gridSize[1]

                pygame.draw.rect(self.display, 
                                    (255,0,0),
                                    (x,y,gridSize[0],gridSize[1]),
                                    1
                                )


class AnimeManager(object):
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((800,600))
        self.animePlayList = []


    def draw(self):
        self.display.fill((0,0,0))

        for obj in self.animePlayList:
            obj.draw()

        pygame.display.update()

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


if __name__ == "__main__":
    main()