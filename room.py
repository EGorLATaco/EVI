import random
import pygame

W, H = 1200, 684
def second_room(room, storona):
    room.way2[room.way2.index(1)] = 0
    room.way2[random.randint(0, 3)] = 1
    while room.way2.index(1) == storona:
        room.way2[room.way2.index(1)] = 0
        room.way2[random.randint(0, 3)] = 1

class Room (pygame.sprite.Sprite):
    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.w = w
        self.h = h
        self.way1 = [0]*4
        self.way2 = [0]*4
        self.way1[random.randint(0, 3)] = 1
        self.way2[random.randint(0, 3)] = 1
        while self.way2.index(1) == self.way1.index(1):
            self.way2[self.way2.index(1)] = 0
            self.way2[random.randint(0, 3)] = 1

    def new_room(self, hero_sprite):
        if hero_sprite.rect.y < H // 7 + 50:
            hero_sprite.rect.y = 4 * H // 6 - 25
            self.way1[self.way1.index(1)] = 0
            self.way1[1] = 1
            second_room(self, 1)
        elif hero_sprite.rect.y > 7 * H // 12:
            hero_sprite.rect.y = H // 6 + 25
            self.way1[self.way1.index(1)] = 0
            self.way1[0] = 1
            second_room(self, 0)
        elif hero_sprite.rect.x > 7 * W // 9:
            hero_sprite.rect.x = W // 9
            self.way1[self.way1.index(1)] = 0
            self.way1[2] = 1
            second_room(self, 2)
        elif hero_sprite.rect.x < W // 9:
            print (1)
            hero_sprite.rect.x = 7 * W // 9
            self.way1[self.way1.index(1)] = 0
            self.way1[3] = 1
            second_room(self, 3)