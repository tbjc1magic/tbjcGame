
import bisect

class AnimeManager:

    def __init__(self):
        self.animeQueue = []

    def add(self, animator, priority=-1):
        bisect.insort(self.animeQueue, [priority,animator])

    def draw(self):
        pass
