import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, [800, 800])

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x -= 0.8
        if keys[pygame.K_LEFT]:
            self.rect.x += 0.8
