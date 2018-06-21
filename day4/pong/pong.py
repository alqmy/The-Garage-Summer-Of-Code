import sys
import pygame

import colors
import racket


# main game function
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pong")

    # Setup elements
    racket.setup(screen)

    # Start the game loop
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # handle events    
            racket.on(event)
        
        # update elements
        racket.update(screen.get_width(), screen.get_height())

        # fill the screen with a black color
        screen.fill(colors.BLACK)

        # draw elements
        racket.draw(screen)
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == "__main__":
    run_game()