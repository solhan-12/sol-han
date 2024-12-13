# some info taught by chatgtp and w3schools
#https://chatgpt.com/c/674f7220-86d8-8004-98c2-f3141858437b (help me learn and create a ball for pong in python)
import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint
# for 2d vectors in the game
vec = pg.math.Vector2

from sprites import *
from setting import *

# main game class
class Game:
    # initionalztion 
    def __init__(self):
        pg.init()
       # setting window and screen size
        self.screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # setting a backround image
        self.backgroundImage = pg.image.load("./background.png").convert()
        self.backgroundImage = pg.transform.smoothscale(self.backgroundImage, self.screen.get_size())
        # setting a window caption title
        pg.display.set_caption("Sol game")
        # setting a clock
        self.clock = pg.time.Clock()
        # printing a screen size just to check
        print(self.screen)
        self.paddal_1 = paddal()  
        self.paddal_2 = paddal()
        self.paddal_1.creating_player1()
        self.paddal_2.creating_player2()
        # spacehips
        self.spacehips = pg.sprite.Group()

        # ball
        self.ball = Ball(10, RED, WINDOW_WIDTH, WINDOW_HEIGHT)
   
    #run function
    def run(self):
        # a variable holding running data
        self.running = True

        # while loop to check a window event and screen drawing 
        while self.running:
            # handle events
            self.events()

            # update
            self.update()
            
            # drawing
            self.draw()   

    # Handling all events
    def events(self):
        # checking if there was any event
        for event in pg.event.get():
            # if there is a Quit event 
            if event.type == pg.QUIT:
                # stop running 
                self.running = False

        # key pressed events
        keys = pg.key.get_pressed()

        # if Up key is pressed, move the paddle up by decreasing its y position
        if keys[pg.K_w]:
            self.paddal_1.move_up()
            
        if keys[pg.K_UP]:
            self.paddal_2.move_up() 

        # if Down key is pressed, move the paddle down by increasing its y position
        if keys[pg.K_DOWN]:
            self.paddal_2.move_downward()
        
        if keys[pg.K_s]:
            self.paddal_1.move_downward()
        # checking if space bar was pessed
        if keys[pg.K_SPACE]:
            self.spacehips.empty()
        #get folder and file
            for i in range(0,9):
                s = Spaceship(100,100,(0,255,0), WINDOW_WIDTH, WINDOW_HEIGHT)
                self.spacehips.add(s)

    # update function
    def update(self):
        self.ball.update()

    # draw function 
    def draw(self):
        # draw the backround
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))
        
        # draw the paddle 
        self.paddal_1.draw(self.screen)
        self.paddal_2.draw(self.screen)

        # draw spaceships
        self.spacehips.draw(self.screen)

        # draw the ball
        self.ball.draw(self.screen)

        # draw the screen
        pg.display.flip()

# created a game object
g = Game()

# run the game
g.run()

# quiting the game
pg.quit()
