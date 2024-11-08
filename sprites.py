import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint

vec = pg.math.Vector2

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
         
