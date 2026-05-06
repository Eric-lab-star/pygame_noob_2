import pygame
from os.path import join

# 수정하기 ─────┐
from settings import all_sprite_group, missile_sprite_group


class Missile(pygame.sprite.Sprite):
    path: str = join("images", "missile.png")
    surf: pygame.Surface = pygame.image.load(path).convert_alpha()
    speed: float = 200

    # 수정하기 ─────┐
    def __init__(
        self,
        pos: pygame.Vector2,
    ):
        # 수정하기 ─────┐
        super().__init__(all_sprite_group, missile_sprite_group)
        self.image = Missile.surf
        self.rect: pygame.FRect = self.image.get_frect(midbottom=(pos))

    def update(self, dt: float):
        self.rect.centery -= dt * Missile.speed
        if self.rect.bottom < 0:
            self.kill()
