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

        # paddles for players
        self.paddle_1 = Paddle(30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)  
        self.paddle_2 = Paddle(950, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

        # spacehips
        self.spacehips = pg.sprite.Group()

        # ball
        self.ball = Ball(10, RED, WINDOW_WIDTH, WINDOW_HEIGHT)

        # fonts
        self.font1 = pg.font.Font(None, 30)
        self.font2 = pg.font.Font(None, 50)
   
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

        # esc to quit
        if keys[pg.K_ESCAPE]:
            self.running = False

        # if Up key is pressed, move the paddle up by decreasing its y position
        if keys[pg.K_w]:
            self.paddle_1.move_up()
            
        if keys[pg.K_UP]:
            self.paddle_2.move_up() 

        # if Down key is pressed, move the paddle down by increasing its y position
        if keys[pg.K_DOWN]:
            self.paddle_2.move_downward()
        
        if keys[pg.K_s]:
            self.paddle_1.move_downward()
        # checking if space bar was pessed
        if keys[pg.K_SPACE]:
            self.spacehips.empty()
        #get folder and file
            for i in range(0,9):
                s = Spaceship(100,100,(0,255,0), WINDOW_WIDTH, WINDOW_HEIGHT)
                self.spacehips.add(s)

    # update function
    def update(self):
        self.paddle_1.collision(self.ball)
        self.paddle_2.collision(self.ball)
        self.ball.update(self.paddle_1, self.paddle_2)

    # draw function 
    def draw(self):
        # draw the backround
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))
        
        # draw the paddle 
        self.paddle_1.draw(self.screen)
        self.paddle_2.draw(self.screen)

        # draw spaceships
        self.spacehips.draw(self.screen)

        # draw the ball
        self.ball.draw(self.screen)

        # draw texts
        text = self.font1.render('W, S for player 1. Up, down for player 2', 1, Black)
        text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + WINDOW_HEIGHT//2-50))
        self.screen.blit(text, text_rect)

        text = self.font2.render('score: ' + str(self.paddle_1.score), 1, Black)
        text_rect = text.get_rect(center=(WINDOW_WIDTH * 0.2, WINDOW_HEIGHT//2 + WINDOW_HEIGHT//2-50))
        self.screen.blit(text, text_rect)

        text = self.font2.render('score: ' + str(self.paddle_2.score), 1, Black)
        text_rect = text.get_rect(center=(WINDOW_WIDTH * 0.8, WINDOW_HEIGHT//2 + WINDOW_HEIGHT//2-50))
        self.screen.blit(text, text_rect)

        # draw the screen
        pg.display.flip()

# created a game object
g = Game()

# run the game
g.run()

# quiting the game
pg.quit()
