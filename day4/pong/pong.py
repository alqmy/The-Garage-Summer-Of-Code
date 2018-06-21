import sys
import pygame


# main game function
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Pong")

    # Start the game loop
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    run_game()