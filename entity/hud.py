from os.path import join
import pygame
from settings import all_sprite_group, WINDOW_HEIGHT, WINDOW_WIDTH


class HUD(pygame.sprite.Sprite):
    path = join("images", "Galmuri9.ttf")
    pygame.font.init()
    font = pygame.font.Font(path, size=50)
    ui = font.render(text=str("game over"), antialias=False, color="white")

    def __init__(self):
        super().__init__(all_sprite_group)
        self.image: pygame.Surface = HUD.ui
        self.rect: pygame.FRect = self.image.get_frect()

    def update(self, dt: float):
        self.rect.center = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
