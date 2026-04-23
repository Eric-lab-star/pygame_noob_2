import pygame
from os.path import join


class Missile(pygame.sprite.Sprite):
    path: str = join("images", "missile.png")
    speed: float = 200

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = pygame.image.load(Missile.path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(center=(100, 100))

    def update(self, dt: float):
        self.rect.centery += Missile.speed * dt

        if self.rect.bottom < 0:
            self.kill()

    def spawn(self, pos: pygame.Vector2):
        self.rect.center = pos
