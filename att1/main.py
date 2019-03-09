import pygame

def main():

    x,y = 50,400
    width, height = 40,60
    xv,yv = 0, 0
    xacc,yacc = 2,-2

    pygame.init()
    clock = pygame.time.Clock()

    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('A bit Racey')
    run = True

    


    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #print(event)

        keys = pygame.key.get_pressed()
        

        
        if keys[pygame.K_LEFT]:
            xv -= xacc

        if keys[pygame.K_RIGHT]:
            xv += xacc
        
        if keys[pygame.K_SPACE]:
            if abs(y-400) <1e-3:
                yv = -30
        
        x,y = x+xv, y+yv

        xv = xv/max(abs(xv),1e-3)*max(abs(xv)-1,0)
        yv -= yacc

        if y >= 400:
            y = 400
            yv = 0


        gameDisplay.fill((0,0,0))
        pygame.draw.rect(gameDisplay, 
                         (255,0,0),
                         (x,y,width,height)
                        )

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()
if __name__ == "__main__":
    main()