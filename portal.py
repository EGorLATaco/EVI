import pygame



class Portal (pygame.sprite.Sprite):
    def __init__(self, w, h, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        image = img
        self.image = pygame.transform.scale(image, (w//5, h//5))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.radius = int(self.rect.width * .85 / 2)
        self.portal_image=0

    def update(self, *args):

        while(self.portal_image<21):
            self.image = args[0][self.portal_image]
            self.portal_image += 1