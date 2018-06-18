import pygame

# COLOR = (ROJO, VERDE, AZUL)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# tamaños
circle_size = 25    # radio del circulo

# posición inicial del circulo
x = 0
y = 0

# 5 pixeles/dibujo
velocidad_y = 5
velocidad_x = 5


# inicializa pygame
pygame.init()

# definir una pantalla
size_pantalla = [800, 600]
pantalla = pygame.display.set_mode(size_pantalla)

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    pantalla.fill(WHITE)

    # dibuja en la pantalla, un circle de color azul
    # en coordenadas 'x' y 'y' de radio circle_size
    pygame.draw.circle(pantalla, BLUE, [x, y], circle_size)

    x = x + velocidad_x
    y = y + velocidad_y

    pygame.display.flip()

pygame.quit()