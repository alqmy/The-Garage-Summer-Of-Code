import pygame
from drawable import Drawable

WHITE = (255,255,255)

class Racket(Drawable):
    def __init__(self, height=50, width=5):
        self.rect = pygame.Rect(0, 0, width, height)
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
    
    def update(self):
        self.rect.top += self.velocity