"""
Racket - module for working with a racket
"""
import pygame
import colors

size = (50, 100)  # 50x100 pixels
position = (0, 0)  # position of the racket
velocity = 0


def setup(screen):
    "Setups the initial position of the racket"
    global position

    (_, height) = screen.get_size()
    (racket_x, _) = position

    # calculate new y position for the racket
    new_y = height / 2 - size[1]

    position = (racket_x, new_y)


def draw(screen):
    "Draws racket on the screen"
    global position
    global size

    (left, top) = position
    (width, height) = size
    rect = pygame.Rect(left, top, width, height)

    pygame.draw.rect(screen, colors.WHITE, rect)


def on(event):
    "Update racket on event"
    global velocity

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            velocity = 5
        elif event.key == pygame.K_UP:
            velocity = -5
    elif event.type == pygame.KEYUP:
        velocity = 0


def update(width, height):
    "update the position of the racket"
    global velocity
    global position
    global size

    (x, y) = position
    (_, racket_height) = size

    new_y = y + velocity

    if new_y < 0:
        new_y = 0
    elif new_y + racket_height > height:
        new_y = height - racket_height

    position = (x, new_y)
