import pygame
from os.path import join
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Player(pygame.sprite.Sprite):
    path: str = join("images", "player.png")
    speed: float = 100
    velocity: pygame.Vector2 = pygame.Vector2(0, 0)

    def __init__(self, group: pygame.sprite.Group):
        super().__init__(group)
        self.image = pygame.image.load(Player.path).convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    def update(self, dt: float):
        keys = pygame.key.get_pressed()
        self.velocity.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.velocity.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

        if self.velocity.length() > 0:
            self.velocity.normalize_ip()

        self.rect.center += self.velocity * Player.speed * dt
