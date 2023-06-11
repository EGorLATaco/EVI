import pygame


class WallPart (pygame.sprite.Sprite):
    def __init__(self, w, h, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('texture/4.png').convert_alpha()
        self.image = pygame.transform.scale(image, (w//9, h//6))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.radius = int(self.rect.width * .85 / 2)