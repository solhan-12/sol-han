import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint
from random import random 

vec = pg.math.Vector2

from setting import *

class Paddle:
    def __init__(self, pos_x, pos_y, size_width, size_height):
        self.pos = vec(pos_x, pos_y)
        self.size = vec(size_width, size_height)
        self.score = 0

    def draw(self,screen):
        # draw the paddle
        pg.draw.rect(screen, Black, (self.pos.x, self.pos.y, self.size.x, self.size.y))

        # draw outline 
        pg.draw.line(screen, YELLOW, vec(self.pos.x, self.pos.y), vec(self.pos.x, self.pos.y + self.size.y))
        pg.draw.line(screen, YELLOW, vec(self.pos.x, self.pos.y + self.size.y), vec(self.pos.x + self.size.x, self.pos.y + self.size.y))
        pg.draw.line(screen, YELLOW, vec(self.pos.x + self.size.x, self.pos.y + self.size.y), vec(self.pos.x + self.size.x, self.pos.y))
        pg.draw.line(screen, YELLOW, vec(self.pos.x + self.size.x, self.pos.y), vec(self.pos.x, self.pos.y))

    def move_up(self):
        # if Up key is pressed, move the paddle up by decreasing its y position
        self.pos.y -= PADDLE_SPEED  

        # if the paddle position is above window, bring it back
        if self.pos.y < 0:
            self.pos.y = 0

        # if the paddle position is below window, bring it back
        if self.pos.y > WINDOW_HEIGHT - self.size.y:
            self.pos.y = WINDOW_HEIGHT - self.size.y

    def move_downward(self):
        # if Down key is pressed, move the paddle down by increasing its y position
        self.pos.y += PADDLE_SPEED  

        # if the paddle position is above window, bring it back
        if self.pos.y < 0:
            self.pos.y = 0

        # if the paddle position is below window, bring it back
        if self.pos.y > WINDOW_HEIGHT - self.size.y:
            self.pos.y = WINDOW_HEIGHT - self.size.y

    def collision(self, ball):
        # left wall
        wall_1 = Wall(vec(self.pos.x, self.pos.y), vec(self.pos.x, self.pos.y + self.size.y), vec(-1, 0))
        wall_1.collision(ball)

        # bottom wall
        wall_2 = Wall(vec(self.pos.x, self.pos.y + self.size.y), vec(self.pos.x + self.size.x, self.pos.y + self.size.y), vec(0, 1))
        wall_2.collision(ball)

        # right wall
        wall_3 = Wall(vec(self.pos.x + self.size.x, self.pos.y + self.size.y), vec(self.pos.x + self.size.x, self.pos.y), vec(1, 0))
        wall_3.collision(ball)

        # top wall
        wall_4 = Wall(vec(self.pos.x + self.size.x, self.pos.y), vec(self.pos.x, self.pos.y), vec(0, -1))
        wall_4.collision(ball)

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

# Wall represents a line segment to bound off a ball
class Wall:
    def __init__(self, pos_1, pos_2, normal):
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.normal = normal.normalize()

    def collision(self, ball):
        dn = (ball.position - self.pos_1).dot(self.normal)
        t = (self.pos_2 - self.pos_1).dot(ball.position - self.pos_1) / (self.pos_2 - self.pos_1).dot((self.pos_2 - self.pos_1))

        if dn >= 0 and dn < ball.radius and t >= 0 and t <= 1.0:
            vn = ball.velocity.dot(self.normal)
            vt = ball.velocity - vn * self.normal

            if (vn < 0):
                ball.velocity = vt + (-vn) * self.normal

            return True

        return False

# Ball object          
class Ball(Sprite):
    def __init__(self, radius, color, window_width, window_height):
        Sprite.__init__(self)
        self.color = color
        self.position = vec(window_width/2, window_height/2)

        # ball's speed
        self.speed = 0.2 

        # ball initial velocity
        self.velocity = self.speed * vec(random(), random()).normalize()

        self.radius = radius
        self.window_width = window_width
        self.window_height = window_height

    # draw the ball on the screen
    def draw(self, screen):
        pg.draw.circle(screen, RED, self.position, self.radius)

    # check collision against screen boundary walls
    def collision(self, paddle_1, paddle_2):
        # left wall
        wall_1 = Wall(vec(0, 0), vec(0, self.window_height), vec(1, 0))
        if wall_1.collision(self):
            paddle_2.score += 1

        # bottom wall
        wall_2 = Wall(vec(0, self.window_height), vec(self.window_width, self.window_height), vec(0, -1))
        wall_2.collision(self)

        # right wall
        wall_3 = Wall(vec(self.window_width, self.window_height), vec(self.window_width, 0), vec(-1, 0))
        if wall_3.collision(self):
            paddle_1.score += 1

        # top wall
        wall_4 = Wall(vec(self.window_width, 0), vec(0, 0), vec(0, 1))
        wall_4.collision(self)

    # update ball's movement
    def update(self, paddle_1, paddle_2):
        self.collision(paddle_1, paddle_2)

        self.position += self.velocity

    

