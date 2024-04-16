import pygame

class Scene:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()

    def _handle_events(self, eventQueue):
        for event in eventQueue.get():
            print(event)
            if event.type == pygame.QUIT:
                return False
        return True