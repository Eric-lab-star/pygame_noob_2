import pygame
from settings import (
    all_sprite_group,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)
from os.path import join


class Hud(pygame.sprite.Sprite):
    #   ┌─ 추가하기
    font_path = join("images", "Galmuri9.ttf")
    #                           ┌─ 추가하기
    font = pygame.font.Font(font_path, size=100)

    def __init__(self, msg=""):
        super().__init__(all_sprite_group)
        self.image: pygame.Surface = Hud.font.render(msg, True, "white")
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    def draw(self, msg: str):
        self.image: pygame.Surface = Hud.font.render(msg, True, "white")
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    def update(self, dt: float):
        pass
