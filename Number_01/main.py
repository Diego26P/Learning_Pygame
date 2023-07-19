import pygame, sys
from player import Player
from bg import Background

pygame.init()
clock = pygame.time.Clock()

vel = 5

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number 01")

object_group = pygame.sprite.Group()
bg = Background("bg.png")
object_group.add(bg)

player = Player("player.png")
object_group.add(player)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        screen.fill((0,0,0))
        object_group.update()
        object_group.draw(screen)
        clock.tick(60)


if __name__ == "__main__":
    main()