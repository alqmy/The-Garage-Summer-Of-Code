from drawable import Drawable
from racket import Racket


def draw_screen(d: Drawable):
    d.draw()


r = Racket()
draw_screen(r)
