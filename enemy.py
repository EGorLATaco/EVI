import pygame
from hero import Hero
W, H = 1200, 684


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img, health, quantity, img_attacks, damage):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
        self.attack = pygame.transform.scale(img_attacks, (img.get_width() * 2, img.get_height() * 2))
        self.rect = self.image.get_rect(center=(x, y))
        self.walk_image = 0
        self.last_side = 3
        self.speed = 5
        self.radius = int(self.rect.width * 0.5)
        self.timer = 0
        self.clock = pygame.time.get_ticks() + 1000
        self.health = health
        self.prov_att = False
        self.damage = damage
        self.k = 0

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y
    def kill_r(self):
        self.kill()

    def __move(self, side):
        if side == 0:
            self.last_side = 0
            self.rect.y -= self.speed
        elif side == 1:
            self.last_side = 1
            self.rect.y += self.speed
        elif side == 3:
            self.last_side = 3
            self.rect.x += self.speed
        elif side == 2:
            self.last_side = 2
            self.rect.x -= self.speed

    def update(self, *args):
        screen = args[6]
        if self.timer % 2 == 1:
            self.walk_image += 1
        self.timer += 1
        if self.timer == 2: self.timer = 0
        if self.walk_image + 1 > 8:
            self.walk_image = 0
        if self.clock < pygame.time.get_ticks():
            hero = args[0]
            x = self.rect.x
            y = self.rect.y
            if abs(hero.rect.x - x) > 100:
                self.prov_att = False
                if hero.rect.x > x:
                    self.__move(3)
                else:
                    self.__move(2)
            elif abs(hero.rect.y - y) > 100:
                self.prov_att = False
                if hero.rect.y > y:
                    self.__move(1)
                else:
                    self.__move(0)
            else:
                self.prov_att = True
                self.speed = 0
                if self.walk_image + 1 > 4:
                    self.walk_image = 0
                if self.last_side == 0:
                    self.attack = args[10][self.walk_image]
                    self.k += 1
                elif self.last_side == 1:
                    self.attack = args[11][self.walk_image]
                    self.k += 1
                elif self.last_side == 2:
                    self.attack = args[9][self.walk_image]
                    self.k += 1
                elif self.last_side == 3:
                    self.attack = args[8][self.walk_image]
                    self.k += 1
                if (self.k > 4):
                    hero.take_damage(self.damage)
                    self.k = 0
                self.attack = pygame.transform.scale(self.attack,
                                                     (self.attack.get_width() * 3, self.attack.get_height() * 3))
                self.speed = 5

            if self.last_side == 0:
                self.image = args[3][self.walk_image]
            elif self.last_side == 1:
                self.image = args[4][self.walk_image]
            elif self.last_side == 2:
                self.image = args[2][self.walk_image]
            elif self.last_side == 3:
                self.image = args[1][self.walk_image]
            prov = args[7]
            attack_power = args[5]
            #health_bar=pygame.draw.line(self.image,(255, 0, 0), (0, 0), (50, 0), 3)
            #health_bar_position = (self.rect.x, self.rect.y - 10)
            #screen.blit(self.image, health_bar_position)
            font = pygame.font.SysFont(None, 25)
            #health_bar = font.render("Health: " + str(self.health), True, (255, 0, 0))
            if (prov):
                self.health -= attack_power
                if self.health <= 0:
                    hero.heal(5)
                    self.kill()

            #screen.blit(health_bar, (self.rect.x, self.rect.y - 10))
            pygame.draw.line(screen, (255, 0, 0),[self.rect.x+20, self.rect.y - 10],[self.rect.x+20+self.health/1.5, self.rect.y - 10], 7)
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
            if (self.prov_att):
                screen.blit(self.attack, self.rect)

            else:
                screen.blit(self.image, self.rect)

        # pygame.transform.scale(self.image, (self.image.get_width()*(args[2]/1200), self.image.get_height()*(args[3]/684)))