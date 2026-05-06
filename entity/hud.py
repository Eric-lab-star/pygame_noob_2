import pygame
from settings import (
    all_sprite_group,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


class Hud(pygame.sprite.Sprite):
    font = pygame.font.Font(size=100)

    def __init__(self):
        super().__init__(all_sprite_group)
        self.image: pygame.Surface = Hud.font.render("Game Over", True, "white")
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def update(self, dt: float):
        pass
