# some info taught by chatgtp and w3schools
#to chat gtp:   (help me learn and create a ball for pong in python)
import pygame as pg
from pygame.sprite import Sprite
import os
from random import randint
# for 2d vectors in the game
vec = pg.math.Vector2

# Colors
WHITE = (255,255,255)
BLUE = (50,50,255)
Black = (0, 0, 0)

# Window size
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# Paddle settings
PADDLE_SPEED = 0.78
PADDLE_WIDTH = 25
PADDLE_HEIGHT = 90

# Spaceship  class from pygame sprite module (initinitializer)
class Spaceship(Sprite):
    def __init__(self, width, height, color):
        Sprite.__init__(self)

        # set the width and height
        self.width = width
        self.height = height

        # load the image (helped by chatgtp)
        self.image = pg.image.load("./spaceship.png").convert_alpha()

        # reszie the player image
        self.image = pg.transform.scale(self.image, (self.width, self.height))

        # set the color
        self.color = color

        # set the rectangle size
        self.rect = pg.Rect(0, 0, self.width, self.height)
        
        # set the center position randomly
        self.rect.center = vec(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))

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
                s = Spaceship(100,100,(0,255,0))
                self.spacehips.add(s)

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

        # draw the screen
        pg.display.flip()

        # Ball class to handle the behavior of the ball in the Pong game
class Ball(Sprite):
    def __init__(self, radius, color, speed):
        # Initialize the Sprite superclass
        Sprite.__init__(self)

        # Set the radius of the ball
        self.radius = radius

        # Set the color of the ball
        self.color = color

        # Create a transparent surface for the ball (allows us to draw the circle)
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)

        # Draw a circle on the ball's surface
        pg.draw.circle(self.image, color, (radius, radius), radius)

        # Get the rectangular bounds of the ball's image for positioning
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        # Set the initial velocity as a vector, determining its movement
        self.velocity = vec(speed, speed)

    # Update method to handle the ball's movement and collisions
    def update(self, paddal_1, paddal_2):
        # Move the ball horizontally and vertically according to its velocity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Check if the ball hits the top or bottom of the screen
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            # Reverse the vertical direction (bounce)
            self.velocity.y *= -1

        # Check if the ball collides with either paddle
        if self.rect.colliderect(paddal_1.get_rect()) or self.rect.colliderect(paddal_2.get_rect()):
            # Reverse the horizontal direction (bounce)
            self.velocity.x *= -1

        # Reset the ball if it goes beyond the left or right edge of the screen
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.reset()

    # Reset method to reposition the ball and randomize its velocity
    def reset(self):
        # Set the ball back to the center of the screen
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Assign a random velocity with a new direction after reset
        self.velocity = vec(randint(-3, 3), randint(-3, 3))



# created a game object
g = Game()

# run the game
g.run()

# quiting the game
pg.quit()
