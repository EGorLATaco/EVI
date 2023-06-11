import pygame
class Enemy_Bullet (pygame.sprite.Sprite):
    def __init__(self, hero, image, w, h, way):
        super(Enemy_Bullet, self).__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=(hero.rect.x, hero.rect.y))
        self.var_image = 0
        self.speed = 30
        self.rect.centerx = hero.rect.centerx
        self.screenW = w
        self.screenH = h
        self.image_height = self.image.get_height()
        self.image_weight = self.image.get_width()
        self.way = way

    def update(self):
        if self.way == 1:
            self.rect.y -= self.speed
        elif self.way == 2:
            self.rect.y += self.speed
        elif self.way == 3:
            self.rect.x -= self.speed
        elif self.way == 4:
            self.rect.x += self.speed
        elif self.way == 5:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.way == 6:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.way == 7:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.way == 8:
            self.rect.x += self.speed
            self.rect.y += self.speed
        self.image = pygame.transform.scale(self.image, (self.image_height * 2, self.image_weight * 2))