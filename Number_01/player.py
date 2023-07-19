import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()

        self.moment = 500
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = [400, 500]

        self.speed = 0
        self.acceleration = 0.01

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_SPACE]:
            self.speed -= self.acceleration
            if self.rect.y >= self.moment - 15:
                while self.rect.y >= self.moment - 15:
                    self.rect.y += 0.2

            self.rect.y = self.speed

        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0