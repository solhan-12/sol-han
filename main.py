
import pygame as pg
import os

# Colors
WHITE = (255,255,255)
BLUE = (50,50,255)
Black = (0, 0, 0)

# Window size
WIDTH = 1000
HEIGHT = 800

# main game class
class Game:
    # initionalztion 
    def __init__(self):
        pg.init()
       # setting window and screen size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # setting a backround image
        self.backgroundImage = pg.image.load("./background.png").convert()
        self.backgroundImage = pg.transform.smoothscale(self.backgroundImage, self.screen.get_size())
        # setting a window caption title
        pg.display.set_caption("Sol game")
        # setting a clock
        self.clock = pg.time.Clock()
        # printing a screen size just to check
        print(self.screen)
        # paddle postion in the y direction
        self.paddle_y = HEIGHT // 2 - 80 // 2 
   
   #run function
    def run(self):
        # a variable holding running data
        running = True

# while loop to check a window event and screen drawing 
        while running:
            # checking if there was any event
            for event in pg.event.get():
                # if there is a Quit event 
                if event.type == pg.QUIT:
                    # stop running 
                    running = False
            
        # draw the backround    
            self.draw()   

    # draw function 
    def draw(self):
        # draw the backround
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))
        
        # draw the paddle 
        pg.draw.rect(self.screen, Black, (50, self.paddle_y, 15, 90))  # Draw the paddle
        pg.display.flip()


# created a game object
g = Game()
# call run function
g.run()
# quiting the game
pg.quit()
