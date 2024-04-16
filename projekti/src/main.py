import pygame

from gameloop import GameLoop
from eventqueue import EventQueue
from scene import Scene
from renderer import Renderer
from clock import Clock

def main():
    height = 600
    width = 800
    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("scuffed solitaire")

    eq = EventQueue()
    cl = Clock()
    sc = Scene()
    rd = Renderer(display, sc)
    gl = GameLoop(sc, rd, eq, cl)

    gl.start()


if __name__ == "__main__":
    main()