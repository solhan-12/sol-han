
import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint

vec = pg.math.Vector2

# Colors
WHITE = (255,255,255)
BLUE = (50,50,255)
Black = (0, 0, 0)

# Window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Paddle settings
PADDLE_SPEED = 2
PADDLE_WIDTH = 25
PADDLE_HEIGHT = 90

# Spaceship sprite class
class Spaceship(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)

        # set the width and height
        self.width = width
        self.height = height

        # load the image
        self.image = pg.image.load("./spaceship.png").convert_alpha()

        # reszie the player image
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        # set the codlor
        self.color = color

        # set the rectangle size
        self.rect = pg.Rect(0, 0, self.width, self.height)
        
        # set the center position randomly
        self.rect.center = vec(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
         
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
        # paddle postion in the y direction
        self.paddle_pos_y = WINDOW_HEIGHT // 2 - 80 // 2 
        # spacehips
        self.spacehips = pg.sprite.Group()
   
    #run function
    def run(self):
        # a variable holding running data
        self.running = True

        # while loop to check a window event and screen drawing 
        while self.running:
            # handle events
            self.events()
            
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
        if keys[pg.K_UP]:
            self.paddle_pos_y -= PADDLE_SPEED  

        # if Down key is pressed, move the paddle down by increasing its y position
        if keys[pg.K_DOWN]:
            self.paddle_pos_y += PADDLE_SPEED  

        # if the paddle position is above window, bring it back
        if self.paddle_pos_y < 0:
            self.paddle_pos_y = 0

        # if the paddle position is below window, bring it back
        if self.paddle_pos_y > WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.paddle_pos_y = WINDOW_HEIGHT - PADDLE_HEIGHT

        if keys[pg.K_SPACE]:
            self.spacehips.empty()
        
            for i in range(0,9):
                s = Spaceship(100,100,(0,255,0))
                self.spacehips.add(s)

    # draw function 
    def draw(self):
        # draw the backround
        self.screen.fill(WHITE)
        self.screen.blit(self.backgroundImage, (0, 0))
        
        # draw the paddle 
        pg.draw.rect(self.screen, Black, (50, self.paddle_pos_y, PADDLE_WIDTH, PADDLE_HEIGHT))

        # draw spaceships
        self.spacehips.draw(self.screen)

        # draw the screen
        pg.display.flip()


# created a game object
g = Game()

# run the game
g.run()

# quiting the game
pg.quit()
