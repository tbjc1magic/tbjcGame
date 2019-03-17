import pygame

def RoundedRect(size,color,radius=0.4):

    rect         = pygame.Rect((0,0,*size))
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return rectangle
    #return surface.blit(rectangle,pos)



if __name__ == "__main__":
    import pkg_resources
    import os

    DATA_PATH = pkg_resources.resource_filename(__name__, 'data')
    fPath = os.path.join(DATA_PATH, 'map.JPG')
    img = pygame.image.load(fPath)

    print(img.get_rect().size)
    scr = pygame.display.set_mode((300,300))
    scr.blit(img,(0,0))

    s = pygame.Surface((400,400))  # the size of your rect
    s.set_alpha(100)                # alpha level
    rr = RoundedRect((100,200),(0,0,255), 0.2)
    s.blit(rr, (50,50))
    #s.fill((0,255,255)) 
    scr.blit(s, (0,0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT: pass