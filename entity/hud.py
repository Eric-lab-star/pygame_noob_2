import pygame
from settings import (
    all_sprite_group,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)


class Hud(pygame.sprite.Sprite):
    font = pygame.font.Font(size=100)

    #                       ┌─ 추가하기
    def __init__(self, msg=""):
        super().__init__(all_sprite_group)
        #                                       ┌─ 추가하기
        self.image: pygame.Surface = Hud.font.render(msg, True, "white")
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    #                   ┌─ 추가하기
    def draw(self, msg: str):
        #                                         ┌─ 추가하기
        self.image: pygame.Surface = Hud.font.render(msg, True, "white")
        self.rect: pygame.FRect = self.image.get_frect(
            center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        )

    def update(self, dt: float):

        pass
