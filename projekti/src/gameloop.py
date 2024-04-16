import pygame

class GameLoop:
    def __init__(self, scene, renderer, eventQueue, clock):
        self._scene = scene
        self._renderer = renderer
        self._eventQueue = eventQueue
        self._clock = clock

    def start(self):
        print("start<")
        while True:
            if self._handle_events() == False:
                print("xd")
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        if not self._scene._handle_events(self._eventQueue):
            print("event quit")
            return False
        
    def _render(self):
        self._renderer.render()
