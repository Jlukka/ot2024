import pygame

class Renderer:
    def __init__(self, display, scene):
        self._display = display
        self._scene = scene

    def render(self):
        self._scene.render(self._display)

        pygame.display.update()