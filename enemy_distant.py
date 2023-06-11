import random
from hero import Hero
import pygame
import math
W, H = 1200, 684
RED = (255, 0, 0)
from enemy_bullet import Enemy_Bullet


class Enemy_Distant (pygame.sprite.Sprite):
    def __init__(self, x, y, img,health,damage,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
        self.rect = self.image.get_rect(center=(x, y))
        self.walk_image = 0
        self.last_side = 3
        self.speed = speed
        self.radius = int(self.rect.width * 0.5)
        self.timer = 0
        self.clock = pygame.time.get_ticks()+1000
        self.health = health
        self.prov_att=False
        self.prov_damage=False
        self.damage=damage
        self.k=0


    def kill_r(self):
        self.kill()
    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y

    def __move (self, side):
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
        arrows_group = pygame.sprite.Group()
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

            if abs(hero.rect.x - x) > 300:
                self.prov_att = False
                self.speed = 10
                if hero.rect.x > x:
                    self.__move(3)
                else:
                    self.__move(2)
            elif abs(hero.rect.y - y) > 200:
                self.prov_att = False
                self.speed = 10
                if hero.rect.y > y:
                    self.__move(1)
                else:
                    self.__move(0)
            else:
                self.prov_att=True
                self.speed = 0

            if self.last_side == 0:
                self.image = args[3][self.walk_image]
            elif self.last_side == 1:
                self.image = args[4][self.walk_image]
            elif self.last_side == 2:
                self.image = args[2][self.walk_image]
            elif self.last_side == 3:
                self.image = args[1][self.walk_image]
            prov=args[7]

            attack_power=args[5]
            #font = pygame.font.SysFont(None, 25)
            #health_bar = font.render("Health: " + str(self.health), True, (255, 0, 0))
            if(prov):
                self.health -= attack_power
                if self.health <= 0:
                    hero.heal(5)
                    self.kill()

            #screen.blit(health_bar, (self.rect.x, self.rect.y - 10))
            pygame.draw.line(screen, (255, 0, 0), [self.rect.x +10, self.rect.y +5],[self.rect.x +10+ self.health / 1.7, self.rect.y + 5], 5)
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
            screen.blit(self.image, self.rect)


        #pygame.transform.scale(self.image, (self.image.get_width()*(args[2]/1200), self.image.get_height()*(args[3]/684)))
