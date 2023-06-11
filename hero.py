import pygame

#hero_sprite.update(pygame.key.get_pressed(), room1.way1, room1.way2, walk_right_surf, walk_left_surf, walk_up_surf, walk_down_surf, collide, W, H,sc, costumes)
#hero_sprite.update(pygame.key.get_pressed(), room1.way1, room1.way2, collide, sc, hero_costumes)

W, H = 1200, 684

class Hero (pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect(center=(x, y))
        self.radius =55
        self.walk_image = 0
        self.last_side = 3
        self.speed = 20
        self.health = 100
        self.timer = 0
        self.clock = pygame.time.get_ticks() + 1000
        self.start_w = self.image.get_width()
        self.start_h = self.image.get_height()
        self.dead_animation = 0
        self.alive = True

    def take_damage(self, damage):
        self.health -= damage
    def heal(self,heal):
        self.health += heal

    def plus_walk(self):
        if self.timer % 2 == 1:
            self.walk_image += 1
        self.timer += 1
        if self.timer == 2: self.timer = 0

    def __move (self, side):
        self.plus_walk()
        if side == 0:
            self.last_side = 0
            self.rect.y -= self.speed
        elif side == 1:
            self.rect.y += self.speed
            self.last_side = 1
        elif side == 3:
            self.rect.x += self.speed
            self.last_side = 3
        else:
            self.rect.x -= self.speed
            self.last_side = 2

    def update(self, *args):


        keys = args[0]
        costumes = args[5]
        if self.health <= 0 and self.alive:
            print(85+self.dead_animation)
            self.image = costumes[86+self.dead_animation]
            self.dead_animation+=1
            if self.dead_animation + 1>6:
                self.alive = False

        elif self.alive:
            if keys[pygame.K_UP]:
                self.__move(0)
            elif keys[pygame.K_DOWN]:
                self.__move(1)
            elif keys[pygame.K_LEFT]:
                self.__move(2)
            elif keys[pygame.K_RIGHT]:
                self.__move(3)


            if not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
                if self.last_side == 0:
                    if self.walk_image >= 8:
                        self.walk_image = 0
                elif self.last_side == 1:
                    if 8 >= self.walk_image or self.walk_image >= 17:
                        self.walk_image = 9
                elif self.last_side == 2:
                    if 17 >= self.walk_image or self.walk_image >= 26:
                        self.walk_image = 18
                elif self.last_side == 3:
                    if 26 >= self.walk_image or self.walk_image >=35:
                        self.walk_image = 27
            if (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):




                if keys[pygame.K_w]:
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.plus_walk()
                        self.last_side = 0
                        if 54 >= self.walk_image or self.walk_image >= 59:
                            self.walk_image = 55
                    else:
                        self.plus_walk()
                        self.last_side = 0
                        if 35 >= self.walk_image or self.walk_image >= 40:
                            self.walk_image = 36
                elif keys[pygame.K_s]:
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.plus_walk()
                        self.last_side = 1
                        if 60 >= self.walk_image or self.walk_image >= 64:
                            self.walk_image = 61
                    else:
                        self.plus_walk()
                        self.last_side = 1
                        if 40 >= self.walk_image or self.walk_image >= 44:
                            self.walk_image = 41
                elif keys[pygame.K_a]:
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.plus_walk()
                        self.last_side = 2
                        if 65 >= self.walk_image or self.walk_image >= 70:
                            self.walk_image = 66
                    else:
                        self.plus_walk()
                        self.last_side = 2
                        if 44 >= self.walk_image or self.walk_image >= 49:
                            self.walk_image = 45
                elif keys[pygame.K_d]:
                    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                        self.plus_walk()
                        self.last_side = 3
                        if 75 >= self.walk_image or self.walk_image >= 80:
                            self.walk_image = 76
                    else:
                        self.plus_walk()
                        self.last_side = 3
                        if 49 >= self.walk_image or self.walk_image >= 54:
                            self.walk_image = 50

            self.image = costumes[self.walk_image]



        collide = args[3]
        screen= args[4]
        font = pygame.font.SysFont(None, 25)
        health_bar = font.render("Health: " + str(self.health), True, (255, 0, 0))
        if self.alive:
            pygame.draw.line(screen, (255, 0, 0), [self.rect.x - 15, self.rect.y -10 ],[self.rect.x -15 + self.health / 1.7, self.rect.y - 10], 7)
            #screen.blit(health_bar, (self.rect.x, self.rect.y - 10))


        if collide:
            # право
            if self.rect.x > 965:
                self.rect.x -= self.speed
            # лево
            if self.rect.x < 123:
                self.rect.x += self.speed
            # вверх
            if self.rect.y < 101:
                self.rect.y += self.speed
            # вниз
            if self.rect.y > 480:
                self.rect.y -= self.speed
        self.image.get_rect(center=(self.rect.x, self.rect.y))





""" if keys[pygame.K_UP]:
            self.__move(0)
        elif keys[pygame.K_DOWN]:
            self.__move(1)
        elif keys[pygame.K_LEFT]:
            self.__move(2)
        elif keys[pygame.K_RIGHT]:
            self.__move(3)
        if not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
            self.number = 0
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or self.number != 0:
            shooting = True
            if keys[pygame.K_d] and shooting:
                self.image = costumes[0][self.number]
                self.last_side = 3
                shooting = False
            elif keys[pygame.K_a] and shooting:
                self.image = costumes[1][self.number]
                self.last_side = 2
                shooting = False
            elif keys[pygame.K_w] and shooting:
                self.image = costumes[3][self.number]
                self.last_side = 0
                shooting = False
            elif keys[pygame.K_s] and shooting:
                self.image = costumes[2][self.number]
                self.last_side = 1
                shooting = False

            if self.number + 1 == len(costumes[3]):
                a =1
            else:
                self.number +=1

        else:
            if self.walk_image + 1 > 9:
                self.walk_image = 0
            if self.last_side == 0:
                self.image = args[5][self.walk_image]
            elif self.last_side == 1:
                self.image = args[6][self.walk_image]
            elif self.last_side == 2:
                self.image = args[4][self.walk_image]
            elif self.last_side == 3:
                self.image = args[3][self.walk_image]"""