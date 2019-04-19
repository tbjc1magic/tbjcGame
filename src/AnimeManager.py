
import bisect

class AnimeManager:

    def __init__(self, display, clockCylce=3):
        self.animeQueue = []
        self.animeManagerClock = -1
        self.animeManagerClockCyle = clockCylce
        self.display = display

    def registerController(self, animator, priority=-1):
        '''
        lowest priority should be map
        highest priority should be move guidance
        '''

        self.animeQueue = sorted(self.animeQueue+[(priority, animator)], 
                                key=lambda _:_[0])
        #bisect.insort(self.animeQueue, [priority,animator])

    def draw(self):

        self.animeManagerClock = (self.animeManagerClock+1) % \
                                 self.animeManagerClockCyle
        
        if self.animeManagerClock>0: return
        self.display.fill((0,0,0))
        for _, animeElement in self.animeQueue:
            animeElement.draw()
        