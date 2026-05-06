from os.path import join
import random
import pygame

#                                   수정하기 ─────┐
from settings import WINDOW_HEIGHT, WINDOW_WIDTH, all_sprite_group, meteor_sprite_group


class Meteor(pygame.sprite.Sprite):
    path: str = join("images", "meteor.png")
    surf: pygame.Surface = pygame.image.load(path).convert_alpha()

    def __init__(self):
        super().__init__(all_sprite_group, meteor_sprite_group)
        self.image: pygame.Surface = Meteor.surf
        self.rect: pygame.FRect = self.image.get_frect(
            center=(random.randint(0, WINDOW_WIDTH), random.randint(-100, 0))
        )
        self.speed: float = random.randint(300, 500)
        self.direction: pygame.Vector2 = pygame.Vector2(random.randint(-1, 1), 1)

    @classmethod
    def spawn(cls, n: int):
        if n <= 0:
            raise ValueError("n must be greater than 0")
        for _ in range(n):
            Meteor()

    def update(self, dt: float):
        self.rect.center += self.direction * dt * self.speed
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
