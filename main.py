
import pygame as pg
import os

# Colors
WHITE = (255,255,255)
BLUE = (50,50,255)

# Window size
WIDTH = 1000
HEIGHT = 800

class Game:
    def __init__(self):
        pg.init()
       
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.backgroundImage = pg.image.load("./background.png").convert()
        self.backgroundImage = pg.transform.smoothscale(self.backgroundImage, self.screen.get_size())
        pg.display.set_caption("Sol game")
        self.clock = pg.time.Clock()
        print(self.screen)

    def run(self):
        self.running = True
        self.playing = True

        while self.running:
            if self.playing == True:
                self.draw()

    def draw(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))
        pg.display.flip()



g = Game()

g.run()

pg.quit()