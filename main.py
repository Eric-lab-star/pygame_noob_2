import pygame

#
from entity.hud import HUD
from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    all_sprite_group,
    meteor_sprite_group,
    missile_sprite_group,
)
from entity.bg import Background

pygame.init()

display_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT),
)

from entity.player import Player
from entity.meteor import Meteor


pygame.display.set_caption("space shooter")


clock = pygame.time.Clock()


def main():
    running = True
    game_over = False
    direction = pygame.Vector2(0, 0)
    bg = Background()
    player = Player()
    hud = HUD()  # <--- 추가
    meteor_event = pygame.event.custom_type()
    if not game_over:
        pygame.time.set_timer(meteor_event, 400)

    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == meteor_event:
                Meteor.spawn(3)
        if direction.length() > 0:
            direction.normalize_ip()

        pygame.sprite.groupcollide(
            meteor_sprite_group, missile_sprite_group, True, True
        )

        #   ┌───── 추가하기
        if not game_over:
            all_sprite_group.update(dt)
            if pygame.sprite.spritecollide(player, meteor_sprite_group, False):
                game_over = True

            all_sprite_group.draw(display_surface)
        else:
            display_surface.blit(bg.image)
            player.kill()
            meteor_sprite_group.empty()

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
