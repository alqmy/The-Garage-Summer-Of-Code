"""
Racket - module for working with a racket
"""
import pygame
import colors

size = 25  # 50 pixels
position = (0, 0)  # position of the racket
velocity = (5, 5)


def setup(resolution=(0,0)):
    "Setups the initial position of the racket"
    global position
    global size

    (width, height) = resolution

    # calculate new y position for the racket
    new_x = int(width / 2)
    new_y = int(height / 2)

    position = (new_x, new_y)


def draw(screen):
    "Draws racket on the screen"
    global position
    global size

    pygame.draw.circle(screen, colors.RED, position, size)


def update(resolution=(0,0)):
    "update the position of the racket"
    global velocity
    global position
    global size

    (x, y) = position
    (vel_x, vel_y) = velocity
    (width, height) = resolution

    x += vel_x
    y += vel_y

    if y + size > height:
        # bottom wall collision
        y = height - size
        vel_y = -vel_y
    elif y - size <= 0:
        # top wall collision
        y = size
        vel_y = -vel_y

    if x + size > width:
        # right wall collision
        x = width - size
        vel_x = -vel_x
    
    velocity = (vel_x, vel_y)
    
    position = (x, y)

def bounce():
    global velocity

    vel_x, vel_y =  velocity

    velocity = (-vel_x, -vel_y)

def collides(rect):
    "Returns if the ball collides with another object"
    left, top = position
    left -= size
    top -= size
    
    circle_rect = pygame.Rect(left, top, size*2, size*2)

    return rect.colliderect(circle_rect)