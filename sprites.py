import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint


vec = pg.math.Vector2


from setting import *


class paddal:
    def __init__(self):
        self.paddle_pos_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
           
    def creating_player2(self):
        self.paddal_pos_x = 950


    def creating_player1(self):
        self.paddal_pos_x = 30


    def draw(self,screen):
     # draw the paddle
        pg.draw.rect(screen, Black, (self.paddal_pos_x, self.paddle_pos_y, PADDLE_WIDTH, PADDLE_HEIGHT))


    def move_up(self):
        # if Up key is pressed, move the paddle up by decreasing its y position
        self.paddle_pos_y -= PADDLE_SPEED  


        # if the paddle position is above window, bring it back
        if self.paddle_pos_y < 0:
            self.paddle_pos_y = 0


        # if the paddle position is below window, bring it back
        if self.paddle_pos_y > WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.paddle_pos_y = WINDOW_HEIGHT - PADDLE_HEIGHT


    def move_downward(self):
        # if Down key is pressed, move the paddle down by increasing its y position
        self.paddle_pos_y += PADDLE_SPEED  


        # if the paddle position is above window, bring it back
        if self.paddle_pos_y < 0:
            self.paddle_pos_y = 0


        # if the paddle position is below window, bring it back
        if self.paddle_pos_y > WINDOW_HEIGHT - PADDLE_HEIGHT:
            self.paddle_pos_y = WINDOW_HEIGHT - PADDLE_HEIGHT


# Spaceship sprite class
class Spaceship(Sprite):
    def __init__(self, width, height, color, window_width, window_height):
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
        self.rect.center = vec(randint(0, window_width), randint(0, window_height))
         
class Ball(Sprite):
    def __init__(self, radius, color, window_width, window_height):
        Sprite.__init__(self)
        self.color = color
        self.position = vec(window_width/2, window_height/2)
        self.velocity = vec(0.1, 0)
        self.radius = radius
        self.window_width = window_width
        self.window_height = window_height


    # draw the ball on the screen
    def draw(self, screen):
        pg.draw.circle(screen, RED, self.position, self.radius)


    # update ball's movement
    def update(self):
        self.position += self.velocity


        if self.position.x > self.window_width:
            self.velocity.x = -self.velocity.x


        if self.position.x < 0:
            self.velocity.x = -self.velocity.x

    

