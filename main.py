import time

import pygame.time
import sys
#поправить collide для разрешения
from boss import *
from enemy import Enemy
from enemy_bullet import *
from enemy_distant import *
from hero import Hero
from portal import Portal
from room import Room
from shot import Bullet
from walls import WallPart


pygame.mixer.init()
pygame.mixer.music.load("music/background.mp3")
pygame.mixer.music.play(-1)
sound_effect1 = pygame.mixer.Sound("music/flames-shot.mp3")
sound_effect2 = pygame.mixer.Sound("music/item-received.mp3")

music_volume = 0.5
sound_volume = 0.5


pygame.init()
pygame.display.set_caption("игруля")

W, H = 1200, 684
w_ratio, h_ratio = W/1200, H/684
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 20
svitok_image=pygame.image.load("texture/fon.png").convert_alpha()
svitok1_image=pygame.image.load("texture/fon1.png").convert_alpha()
svitok2_image=pygame.image.load("texture/fon2.png").convert_alpha()
ui_background_image = pygame.image.load("texture/ui/bg.png").convert_alpha()
font = pygame.font.Font("font.ttf", 36)
play_text = font.render("Играть", True, (255, 255, 255))
settings_text = font.render("Настройки", True, (255, 255, 255))
exit_text = font.render("Выйти", True, (255, 255, 255))
pause_text = font.render("Вернуться", True, (255, 255, 255))
play_button_image = pygame.image.load("texture/ui/button.png").convert_alpha()
settings_button_image = pygame.image.load("texture/ui/button.png").convert_alpha()
exit_button_image = pygame.image.load("texture/ui/button.png").convert_alpha()
ui_background_image = pygame.transform.scale(ui_background_image, (W, H))
play_button_image_pressed = pygame.image.load("texture/ui/button_pressed.png").convert_alpha()
settings_button_image_pressed = pygame.image.load("texture/ui/button_pressed.png").convert_alpha()
exit_button_image_pressed = pygame.image.load("texture/ui/button_pressed.png").convert_alpha()
play_cur = play_button_image
settings_cur = settings_button_image
exit_cur = exit_button_image
button_width = 240
button_height = 60
play_button_x = W // 2 - button_width // 2
play_button_y = 150 * 1.2
settings_button_x = W // 2 - button_width // 2
settings_button_y = 270 * 1.2
exit_button_x = W // 2 - button_width // 2
exit_button_y = 390 * 1.2
game_title_x = (W // 2 - 130* 1.2)
game_title_y = 60


bg = pygame.image.load('texture/1.png').convert_alpha()
bg = pygame.transform.scale(bg, (bg.get_width()*0.7, bg.get_height()*0.7))
room2 = pygame.image.load('texture/3.png').convert_alpha()
room2 = pygame.transform.scale(room2, (bg.get_width()*0.1*w_ratio, bg.get_height()*0.1*h_ratio))

walk_images = [str(i) for i in range(1, 10)]
"""walk_right_surf = [pygame.image.load('walk_right/'+path + '.png').convert_alpha() for path in walk_images]
walk_left_surf = [pygame.image.load('walk_left/'+path + '.png').convert_alpha() for path in walk_images]
walk_up_surf = [pygame.image.load('walk_up/'+path + '.png').convert_alpha() for path in walk_images]
walk_down_surf = [pygame.image.load('walk_down/'+path + '.png').convert_alpha() for path in walk_images]"""
walk_right_surf = [pygame.image.load('walk left prosto/'+path + '.png').convert_alpha() for path in walk_images]
walk_left_surf = []
for i in walk_right_surf:
    walk_left_surf.append(pygame.transform.flip(i, 1, 0))
walk_down_surf = [pygame.image.load('walk down prosto/'+path + '.png').convert_alpha() for path in walk_images]
walk_up_surf = [pygame.image.load('walk up surf/'+path + '.png').convert_alpha() for path in walk_images]
walk_images = [str(i) for i in range (1,6)]
right_shoot = [pygame.image.load('shot_upright/'+path + '.png').convert_alpha() for path in walk_images]
left_shoot = []
for i in right_shoot:
    left_shoot.append(pygame.transform.flip(i, 1, 0))

walk_images = [str(i) for i in range (1,7)]
up_while_walk = [pygame.image.load('shot_walkup/while_walking/'+path + '.png').convert_alpha() for path in walk_images]
walk_images = [str(i) for i in range (1,6)]
down_while_walk = [pygame.image.load('shot_walkdown/while_walking/'+path + '.png').convert_alpha() for path in walk_images]
walk_images = [str(i) for i in range (1,5)]
down_shoot = [pygame.image.load('shot_walkdown/'+path + '.png').convert_alpha() for path in walk_images]
walk_images = [str(i) for i in range (1,6)]
up_shoot = [pygame.image.load('shot_walkup/'+path + '.png').convert_alpha() for path in walk_images]
walk_images = [str(i) for i in range(1,11)]
right_while_walk = [pygame.image.load('shot_upright/shot_while_walk/'+path + '.png').convert_alpha() for path in walk_images]
left_while_walk = []
for i in right_while_walk:
    left_while_walk.append(pygame.transform.flip(i, 1, 0))
walk_images = [str(i) for i in range(1,7)]
dead_surf = [pygame.image.load('hurt/'+path + '.png').convert_alpha() for path in walk_images]
costumes = [walk_up_surf, walk_down_surf, walk_left_surf, walk_right_surf, up_shoot, down_shoot, left_shoot,  right_shoot,up_while_walk, down_while_walk, left_while_walk, right_while_walk, dead_surf]
hero_costumes = []
for i in costumes:
    for j in i:
        hero_costumes.append(pygame.transform.scale(j, (j.get_width()*2, j.get_height()*2)))

martin_images=[str(i) for i in range(1, 9)]

martin_surf_right = [pygame.image.load('martin/walk/' + path + '.png').convert_alpha() for path in martin_images]
martin_surf_down = []
for martin in martin_surf_right:
    martin_surf_down.append(pygame.transform.flip(martin, 1,0))
martin_surf_left = []
for martin in martin_surf_right:
    martin_surf_left.append(pygame.transform.flip(martin, 1,0))
martin_surf_up = []
for martin in martin_surf_right:
    martin_surf_up.append(pygame.transform.flip(martin, 1,0))

martin_attack_images=[str(i) for i in range(1, 5)]

martin_attack_surf_right = [pygame.image.load('martin/attack/' + path + '.png').convert_alpha() for path in martin_attack_images]
martin_attack_surf_down = []
for martin in martin_attack_surf_right:
    martin_attack_surf_down.append(pygame.transform.flip(martin, 1, 0))
martin_attack_surf_left = []
for martin in martin_attack_surf_right:
    martin_attack_surf_left.append(pygame.transform.flip(martin, 1,0))
martin_attack_surf_up = []
for martin in martin_attack_surf_right:
    martin_attack_surf_up.append(pygame.transform.flip(martin, 1,0))


hashashin_images=[str(i) for i in range(1, 9)]

hashashin_surf_right = [pygame.image.load('hashashin/run/' + path + '.png').convert_alpha() for path in martin_images]
hashashin_surf_down = []
for hashashin in hashashin_surf_right:
    hashashin_surf_down.append(pygame.transform.flip(hashashin, 1,0))
hashashin_surf_left = []
for hashashin in hashashin_surf_right:
    hashashin_surf_left.append(pygame.transform.flip(hashashin, 1,0))
hashashin_surf_up = []
for hashashin in hashashin_surf_right:
    hashashin_surf_up.append(pygame.transform.flip(hashashin, 1,0))

hashashin_attack_images=[str(i) for i in range(1, 9)]

hashashin_attack_surf_right = [pygame.image.load('hashashin/attack/' + path + '.png').convert_alpha() for path in martin_attack_images]
hashashin_attack_surf_down = []
for hashashin in hashashin_attack_surf_right:
    hashashin_attack_surf_down.append(pygame.transform.flip(hashashin, 1, 0))
hashashin_attack_surf_left = []
for hashashin in hashashin_attack_surf_right:
    hashashin_attack_surf_left.append(pygame.transform.flip(hashashin, 1,0))
hashashin_attack_surf_up = []
for hashashin in hashashin_attack_surf_right:
    hashashin_attack_surf_up.append(pygame.transform.flip(hashashin, 1,0))


ground_images=[str(i) for i in range(1, 9)]

ground_surf_right = [pygame.image.load('ground/run/' + path + '.png').convert_alpha() for path in ground_images]
ground_surf_down = []
for ground in ground_surf_right:
    ground_surf_down.append(pygame.transform.flip(ground, 1,0))
ground_surf_left = []
for ground in ground_surf_right:
    ground_surf_left.append(pygame.transform.flip(ground, 1,0))
ground_surf_up = []
for ground in ground_surf_right:
    ground_surf_up.append(pygame.transform.flip(ground, 1,0))

ground_attack_images=[str(i) for i in range(1, 9)]

ground_attack_surf_right = [pygame.image.load('ground/attack/' + path + '.png').convert_alpha() for path in ground_attack_images]
ground_attack_surf_down = []
for ground in ground_attack_surf_right:
    ground_attack_surf_down.append(pygame.transform.flip(ground, 1, 0))
ground_attack_surf_left = []
for ground in ground_attack_surf_right:
    ground_attack_surf_left.append(pygame.transform.flip(ground, 1,0))
ground_attack_surf_up = []
for ground in ground_attack_surf_right:
    ground_attack_surf_up.append(pygame.transform.flip(ground, 1,0))

water_images=[str(i) for i in range(1, 9)]

water_surf_right = [pygame.image.load('water/run/' + path + '.png').convert_alpha() for path in water_images]
water_surf_down = []
for water in water_surf_right:
    water_surf_down.append(pygame.transform.flip(water, 1,0))
water_surf_left = []
for water in water_surf_right:
    water_surf_left.append(pygame.transform.flip(water, 1,0))
water_surf_up = []
for water in water_surf_right:
    water_surf_up.append(pygame.transform.flip(water, 1,0))

water_attack_images=[str(i) for i in range(1, 8)]

water_attack_surf_right = [pygame.image.load('water/attack/' + path + '.png').convert_alpha() for path in water_attack_images]
water_attack_surf_down = []
for water in water_attack_surf_right:
    water_attack_surf_down.append(pygame.transform.flip(water, 1, 0))
water_attack_surf_left = []
for water in water_attack_surf_right:
    water_attack_surf_left.append(pygame.transform.flip(water, 1,0))
water_attack_surf_up = []
for water in water_attack_surf_right:
    water_attack_surf_up.append(pygame.transform.flip(water, 1,0))


fire_images=[str(i) for i in range(1, 9)]

fire_surf_right = [pygame.image.load('fire/run/' + path + '.png').convert_alpha() for path in fire_images]
fire_surf_down = []
for fire in fire_surf_right:
    fire_surf_down.append(pygame.transform.flip(fire, 1,0))
fire_surf_left = []
for fire in fire_surf_right:
    fire_surf_left.append(pygame.transform.flip(fire, 1,0))
fire_surf_up = []
for fire in fire_surf_right:
    fire_surf_up.append(pygame.transform.flip(fire, 1,0))

fire_attack_images=[str(i) for i in range(1, 9)]

fire_attack_surf_right = [pygame.image.load('fire/attack/' + path + '.png').convert_alpha() for path in fire_attack_images]
fire_attack_surf_down = []
for fire in fire_attack_surf_right:
    fire_attack_surf_down.append(pygame.transform.flip(fire, 1, 0))
fire_attack_surf_left = []
for fire in fire_attack_surf_right:
    fire_attack_surf_left.append(pygame.transform.flip(fire, 1,0))
fire_attack_surf_up = []
for fire in fire_attack_surf_right:
    fire_attack_surf_up.append(pygame.transform.flip(fire, 1,0))

demon_images=[str(i) for i in range(1, 9)]

demon_surf_left = [pygame.image.load('demon/' + path + '.png').convert_alpha() for path in demon_images]
demon_surf_down = []
for demon in demon_surf_left:
    demon_surf_down.append(pygame.transform.flip(demon, 1,0))
demon_surf_right = []
for demon in demon_surf_left:
    demon_surf_right.append(pygame.transform.flip(demon, 1,0))
demon_surf_up = []
for demon in demon_surf_left:
    demon_surf_up.append(pygame.transform.flip(demon, 1,0))

goblin_images=[str(i) for i in range(1, 9)]

goblin_surf_left = [pygame.image.load('goblin/' + path + '.png').convert_alpha() for path in goblin_images]
goblin_surf_up = []
for goblin in goblin_surf_left:
    goblin_surf_up.append(pygame.transform.flip(goblin, 1,0))
goblin_surf_right = []
for goblin in goblin_surf_left:
    goblin_surf_right.append(pygame.transform.flip(goblin, 1,0))
goblin_surf_down = []
for goblin in goblin_surf_left:
    goblin_surf_down.append(pygame.transform.flip(goblin, 1,0))


boss_images=[str(i) for i in range(1, 13)]

boss_surf_left = [pygame.image.load('boss/walk/' + path + '.png').convert_alpha() for path in boss_images]
boss_surf_down = []
for boss in boss_surf_left:
    boss_surf_down.append(pygame.transform.flip(boss, 1,0))
boss_surf_right = []
for boss in boss_surf_left:
    boss_surf_right.append(pygame.transform.flip(boss, 1,0))
boss_surf_up = []
for boss in boss_surf_left:
    boss_surf_up.append(pygame.transform.flip(boss, 1,0))

boss_attack_images=[str(i) for i in range(1, 16)]

boss_attack_surf_right = [pygame.image.load('boss/attack/' + path + '.png').convert_alpha() for path in boss_attack_images]
boss_attack_surf_down = []
for boss in boss_attack_surf_right:
    boss_attack_surf_down.append(pygame.transform.flip(boss, 1, 0))
boss_attack_surf_left = []
for boss in boss_attack_surf_right:
    boss_attack_surf_left.append(pygame.transform.flip(boss, 1,0))
boss_attack_surf_up = []
for boss in boss_attack_surf_right:
    boss_attack_surf_up.append(pygame.transform.flip(boss, 1,0))

boss_death_images=[str(i) for i in range(1, 23)]

boss_death_surf_left = [pygame.image.load('boss/death/' + path + '.png').convert_alpha() for path in boss_death_images]
boss_death_surf_down = []
for boss_death in boss_death_surf_left:
    boss_death_surf_down.append(pygame.transform.flip(boss_death, 1,0))
boss_death_surf_right = []
for boss_death in boss_death_surf_left:
    boss_death_surf_right.append(pygame.transform.flip(boss_death, 1,0))
boss_death_surf_up = []
for boss_death in boss_death_surf_left:
    boss_death_surf_up.append(pygame.transform.flip(boss_death, 1,0))


bullet_images = [str(i) for i in range(1, 4)]
bullet_surf_up = [pygame.image.load('ball/' + path + '.png').convert_alpha() for path in bullet_images]
bullet_surf_down = []
for bullet in bullet_surf_up:
    bullet_surf_down.append(pygame.transform.flip(bullet, 0, 1))
bullet_surf_right = []
for bullet in bullet_surf_up:
    bullet_surf_right.append(pygame.transform.rotate(bullet, 270))
bullet_surf_left = []
for bullet in bullet_surf_up:
    bullet_surf_left.append(pygame.transform.rotate(bullet, 90))
bullet_up_right = []
for bullet in bullet_surf_up:
    bullet_up_right.append(pygame.transform.rotate(bullet, 315))
bullet_up_left = []
for bullet in bullet_surf_up:
    bullet_up_left.append(pygame.transform.rotate(bullet, 45))
bullet_down_left = []
for bullet in bullet_surf_up:
    bullet_down_left.append(pygame.transform.rotate(bullet, 135))
bullet_down_right = []
for bullet in bullet_surf_up:
    bullet_down_right.append(pygame.transform.rotate(bullet, 225))

bullet_enemy_images = [str(i) for i in range(1, 4)]

bullet_enemy_surf_up = [pygame.image.load('enemy_ball/' + path + '.png').convert_alpha() for path in bullet_enemy_images]
bullet_enemy_surf_down = []
for bullet_enemy in bullet_enemy_surf_up:
    bullet_enemy_surf_down.append(pygame.transform.flip(bullet_enemy, 0, 1))
bullet_enemy_surf_right = []
for bullet_enemy in bullet_enemy_surf_up:
    bullet_enemy_surf_right.append(pygame.transform.rotate(bullet_enemy, 270))
bullet_enemy_surf_left = []
for bullet_enemy in bullet_enemy_surf_up:
    bullet_enemy_surf_left.append(pygame.transform.rotate(bullet_enemy, 90))

green_bullet_enemy_images = [str(i) for i in range(1, 4)]

green_bullet_enemy_surf_up = [pygame.image.load('green_ball/' + path + '.png').convert_alpha() for path in green_bullet_enemy_images]
green_bullet_enemy_surf_down = []
for green_bullet_enemy in green_bullet_enemy_surf_up:
    green_bullet_enemy_surf_down.append(pygame.transform.flip(green_bullet_enemy, 0, 1))
green_bullet_enemy_surf_right = []
for green_bullet_enemy in green_bullet_enemy_surf_up:
    green_bullet_enemy_surf_right.append(pygame.transform.rotate(green_bullet_enemy, 270))
green_bullet_enemy_surf_left = []
for green_bullet_enemy in green_bullet_enemy_surf_up:
    green_bullet_enemy_surf_left.append(pygame.transform.rotate(green_bullet_enemy, 90))

"""for i in enemy_surf:
    pygame.transform.scale(i, (i.get_width()*4, i.get_height()*4))"""
hero_x = W//2
hero_y = H//2
hero_sprite = Hero(hero_x, hero_y, walk_right_surf[0])
ghero=pygame.sprite.Group()
ghero.add(hero_sprite)
room1 = Room(W, H)
var_w = W//9
var_h = H//6

portal_images = [str(i) for i in range(1, 22)]
portal_surf = [pygame.image.load('portal/green/'+path + '.png').convert_alpha() for path in portal_images]


wall_part = pygame.image.load('texture/4.png').convert_alpha()
wall_part = pygame.transform.scale(wall_part, (W//9, H//6))
pygame.sprite.collide_rect_ratio(0.8)

pygame.sprite.collide_rect_ratio(0.8)
bullet = pygame.sprite.Group()

bullet_timer = 0
bullet_enemy_1_timer = 0
bullet_enemy_2_timer = 0

restart_game=False
def show_text_screen():

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

        sc.fill((0, 0, 0))
        sc.blit(svitok1_image,(0,0))
        font = pygame.font.SysFont('segoe print', 18)
        """text = font.render(("В когда-то процветающем королевстве Бангвиль сейчас творится ужас и разгром.  "), True, (255, 0, 0))
        sc.blit(text, (W//2 - 550, H//2 - 150))

        text1 = font.render(("Демон задурманил их разум и подчинил их себе и посылает их бесчинствовать."), True, (255, 0, 0))
        sc.blit(text1, (W // 2 - 550, H // 2 - 100))

        text2 = font.render(("Всё из-за демона Азазеля, который уже 20 лет насылает своих бесов на людей."), True, (255, 0 ,0))
        sc.blit(text2, (W // 2 - 550, H // 2 - 50))

        text3 = font.render(("Уже многие пытались победить его. ") , True, (255, 0, 0))
        sc.blit(text3, (W // 2 - 550, H // 2 ))

        text4 = font.render(("С ним сражались лучшие рыцари королевства, самураи, асcасины, монахи и даже атланты, но у ни у кого не получилось."),True, (255, 0, 0))
        sc.blit(text4, (W // 2 - 550, H // 2 +50))

        text5 = font.render(("Ради возвращения счастливых времен главные маги Бангвиля возродили первого короля, создавшего королевство – EVI … "),True, (255, 0, 0))
        sc.blit(text5, (W // 2 - 550, H // 2 + 100))"""
        

        button_rect_text = font.render(("Играть"), True, (255, 0, 0))
        sc.blit(button_rect_text, (W//2, H//2 + 200))

        button_width = 200
        button_height = 50
        button_x = W // 2 - button_width // 2
        button_y = H - 150
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.display.update()
        clock.tick(60)
text_screen = True

def new_bullet (bullet_timer, time, array, bullet, way):
    if bullet_timer + 200 < time:
        bullet_timer = time
        new_bullet = Bullet(hero_sprite, array[0], W, H, way)
        bullet.add(new_bullet)
    return bullet_timer
def new_bullet_enemy_1 (bullet_timer, time, array, bullet_enemy, way):
    if bullet_timer + 500 < time:
        bullet_timer = time
        new_bullet_enemy = Enemy_Bullet(enemies_sprite_distant_1, array[0], W, H, way)
        bullet_enemy.add(new_bullet_enemy)
    return bullet_timer
def new_bullet_enemy_2 (bullet_timer, time, array, bullet_enemy, way):
    if bullet_timer + 500 < time:
        bullet_timer = time
        new_bullet_enemy = Enemy_Bullet(enemies_sprite_distant_2, array[0], W, H, way)
        bullet_enemy.add(new_bullet_enemy)
    return bullet_timer
def new_bullet_boss (bullet_timer, time, array, bullet_enemy, way):
    if bullet_timer + 2000 < time:
        bullet_timer = time
        new_bullet_enemy = Enemy_Bullet(boss_sprite, array[0], W, H, way)
        bullet_enemy.add(new_bullet_enemy)
    return bullet_timer

def new_room(way1, way2):
    walls = pygame.sprite.Group()
    for i in range(9):
        walls.add(WallPart(W, H, var_w * i, 0))
    for i in range(1, 9):
        walls.add(WallPart(W, H, var_w * i, H - wall_part.get_height()))
    for i in range(6):
        walls.add(WallPart(W, H, 0, var_h * i))
    for i in range(1, 6):
        walls.add(WallPart(W, H, W - wall_part.get_width(), var_h * i))
    return walls

def new_room_portal(way1, way2):
    portal = pygame.sprite.Group()
    image = portal_surf[0]
    img = pygame.transform.scale(image, (0, 0))
    print(way1.index(1), way2.index(1))
    if way1.index(1) == 0 or way2.index(1) == 0:
        portal.add(Portal(W, H, W//2-W//9, 0,img))
    if way1.index(1) == 1 or way2.index(1) == 1:
        portal.add(Portal(W, H,W//2-W//9, 19*H//24,img))
    if way1.index(1) == 2 or way2.index(1) == 2:
        portal.add(Portal(W, H, -30, 5*H//12,img))
    if way1.index(1) == 3 or way2.index(1) == 3:
        portal.add(Portal(W, H, 15*W//18, 5*H//12,img))
    return portal
def new_room_portal_update(way1, way2):
    portal = pygame.sprite.Group()
    if way1.index(1) == 0 or way2.index(1) == 0:
        portal.add(Portal(W, H, W // 2 - W // 9, 0, portal_surf[8]))
        #portal.update(W, H, W//2-W//9, 0,portal_surf)
    if way1.index(1) == 1 or way2.index(1) == 1:
        portal.add(Portal(W, H, W // 2 - W // 9, 19 * H // 24, portal_surf[8]))
        #portal.update(W, H,W//2-W//9, 19*H//24,portal_surf)
    if way1.index(1) == 2 or way2.index(1) == 2:
        portal.add(Portal(W, H, -30, 5 * H // 12, portal_surf[8]))
        #portal.update(W, H, -30, 5*H//12,portal_surf)
    if way1.index(1) == 3 or way2.index(1) == 3:
        portal.add(Portal(W, H, 15 * W // 18, 5 * H // 12, portal_surf[8]))
        #portal.update(W, H, 15*W//18, 5*H//12,portal_surf)

    return portal

walls = new_room(room1.way1, room1.way2)
schet=9

def enemy_update(n):
    if n == 1:
        enB_d1 = pygame.sprite.groupcollide(enemies_1, bullet, False, True)
        enb1_d1=pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_1)
        enemies_1.update(hero_sprite, goblin_surf_right,goblin_surf_left,goblin_surf_up, goblin_surf_down, 10, sc, enB_d1,enb1_d1)
        enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
        enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
        enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc,enB_d2, enb1_d2)
        enB = pygame.sprite.groupcollide(enemies_3, bullet, False, True)
        enemies_3.update(hero_sprite, fire_surf_right,fire_surf_left,fire_surf_up, fire_surf_down, 10, sc, enB,fire_attack_surf_right, fire_attack_surf_left,fire_attack_surf_up, fire_attack_surf_down)
    if n == 2:
        enB_d1 = pygame.sprite.groupcollide(enemies_1, bullet, False, True)
        enb1_d1 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_1)
        enemies_1.update(hero_sprite, goblin_surf_right, goblin_surf_left, goblin_surf_up, goblin_surf_down, 10, sc,enB_d1, enb1_d1)
        enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
        enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
        enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc, enB_d2,enb1_d2)
        enB = pygame.sprite.groupcollide(enemies_3, bullet, False, True)
        enemies_3.update(hero_sprite, martin_surf_right,martin_surf_left,martin_surf_up, martin_surf_down, 10, sc, enB,martin_attack_surf_right, martin_attack_surf_left,martin_attack_surf_up, martin_attack_surf_down)
    if n == 3:
        enB_d1 = pygame.sprite.groupcollide(enemies_1, bullet, False, True)
        enb1_d1 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_1)
        enemies_1.update(hero_sprite, goblin_surf_right, goblin_surf_left, goblin_surf_up, goblin_surf_down, 10, sc,enB_d1, enb1_d1)
        enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
        enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
        enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc, enB_d2,enb1_d2)
        enB = pygame.sprite.groupcollide(enemies_3, bullet, False, True)
        enemies_3.update(hero_sprite, hashashin_surf_right,hashashin_surf_left,hashashin_surf_up, hashashin_surf_down, 10, sc, enB,hashashin_attack_surf_right, hashashin_attack_surf_left,hashashin_attack_surf_up, hashashin_attack_surf_down)
    if n == 4:
        enB_d1 = pygame.sprite.groupcollide(enemies_1, bullet, False, True)
        enb1_d1 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_1)
        enemies_1.update(hero_sprite, goblin_surf_right, goblin_surf_left, goblin_surf_up, goblin_surf_down, 10, sc,enB_d1, enb1_d1)
        enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
        enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
        enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc, enB_d2,enb1_d2)
        enB = pygame.sprite.groupcollide(enemies_3, bullet, False, True)
        enemies_3.update(hero_sprite, ground_surf_right,ground_surf_left,ground_surf_up, ground_surf_down, 10, sc, enB,ground_attack_surf_right, ground_attack_surf_left,ground_attack_surf_up, ground_attack_surf_down)
    if n == 5:
        enB_d1 = pygame.sprite.groupcollide(enemies_1, bullet, False, True)
        enb1_d1 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_1)
        enemies_1.update(hero_sprite, goblin_surf_right, goblin_surf_left, goblin_surf_up, goblin_surf_down, 10, sc,enB_d1, enb1_d1)
        enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
        enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
        enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc, enB_d2,enb1_d2)
        enB = pygame.sprite.groupcollide(enemies_3, bullet, False, True)
        enemies_3.update(hero_sprite, water_surf_right,water_surf_left,water_surf_up, water_surf_down, 10, sc, enB,water_attack_surf_right, water_attack_surf_left,water_attack_surf_up, water_attack_surf_down)

def boss_update():
    enB_d2 = pygame.sprite.groupcollide(enemies_2, bullet, False, True)
    enb1_d2 = pygame.sprite.spritecollideany(hero_sprite, bullet_enemy_2)
    enemies_2.update(hero_sprite, demon_surf_right, demon_surf_left, demon_surf_up, demon_surf_down, 10, sc, enB_d2,enb1_d2)
    enB = pygame.sprite.groupcollide(boss, bullet, False, True)
    boss.update(hero_sprite, boss_surf_right, boss_surf_left, boss_surf_up, boss_surf_down, 10, sc, enB,boss_attack_surf_left, boss_attack_surf_right, boss_attack_surf_up, boss_attack_surf_down)

def show_setting_screen():
    global music_volume, sound_volume
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running = False

                if music_up_button_rect.collidepoint(event.pos):
                    music_volume += 0.1
                    if music_volume > 1.0:
                        music_volume = 1.0
                    pygame.mixer.music.set_volume(music_volume)

                if music_down_button_rect.collidepoint(event.pos):
                    music_volume -= 0.1
                    if music_volume < 0.0:
                        music_volume = 0.0
                    pygame.mixer.music.set_volume(music_volume)

                if sound_up_button_rect.collidepoint(event.pos):
                    sound_volume += 0.1
                    if sound_volume > 1.0:
                        sound_volume = 1.0
                    sound_effect1.set_volume(sound_volume)
                    sound_effect2.set_volume(sound_volume)

                if sound_down_button_rect.collidepoint(event.pos):
                    sound_volume -= 0.1
                    if sound_volume < 0.0:
                        sound_volume = 0.0
                    sound_effect1.set_volume(sound_volume)
                    sound_effect2.set_volume(sound_volume)

        sc.blit(ui_background_image, (0, 0))

        music_text = font.render("Музыка", True, (255, 255, 255))
        sc.blit(music_text, (W // 2 - music_text.get_width() // 2, H // 2 - 50))

        music_volume_text = font.render(str(int(music_volume * 100)) + "%", True, (255, 255, 255))
        sc.blit(music_volume_text, (W // 2 - music_volume_text.get_width() // 2, H // 2))

        music_up_text = font.render("+", True, (255, 255, 255))
        music_down_text = font.render("-", True, (255, 255, 255))

        music_up_button_rect = pygame.Rect(W // 2 + 50, H // 2 - 10, 30, 30)
        sc.blit(music_up_text, (music_up_button_rect.x + 8, music_up_button_rect.y + 6))

        music_down_button_rect = pygame.Rect(W // 2 - 80, H // 2 - 10, 30, 30)
        sc.blit(music_down_text, (music_down_button_rect.x + 8, music_down_button_rect.y + 6))

        sound_text = font.render("Эффекты", True, (255, 255, 255))
        sc.blit(sound_text, (W // 2 - sound_text.get_width() // 2, H // 2 + 100))

        sound_volume_text = font.render(str(int(sound_volume * 100)) + "%", True, (255, 255, 255))
        sc.blit(sound_volume_text, (W // 2 - sound_volume_text.get_width() // 2, H // 2 + 150))

        sound_up_text = font.render("+", True, (255, 255, 255))
        sound_down_text = font.render("-", True, (255, 255, 255))

        sound_up_button_rect = pygame.Rect(W // 2 + 50, H // 2 + 140, 30, 30)
        sc.blit(sound_up_text, (sound_up_button_rect.x + 8, sound_up_button_rect.y + 6))

        sound_down_button_rect = pygame.Rect(W // 2 - 80, H // 2 + 140, 30, 30)
        sc.blit(sound_down_text, (sound_down_button_rect.x + 9, sound_down_button_rect.y + 6))

        back_button_rect = pygame.Rect(20, 20, 100, 50)

        back_text = font.render("Назад", True, (255, 255, 255))
        sc.blit(back_text, (25, 30))

        pygame.display.update()
        clock.tick(60)



def show_game_over_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game=True
                    running = False
                    enemies_sprite.kill()
                    enemies_sprite_distant_1.kill()
                    enemies_sprite_distant_2.kill()
                    hero_sprite.health = 100
                    hero_sprite.rect.x = W // 2
                    hero_sprite.rect.y = H // 2


                elif event.key == pygame.K_q:

                    pygame.quit()
                    sys.exit()

        sc.fill((0, 0, 0))

        game_over_text = font.render("Game Over", True, (255, 0, 0))
        sc.blit(game_over_text,
                (W // 2 - game_over_text.get_width() // 2, H // 2 - game_over_text.get_height() // 2))

        restart_text = font.render("Press 'R' to restart", True, (255, 255, 255))
        sc.blit(restart_text, (W // 2 - restart_text.get_width() // 2, H // 2 + restart_text.get_height()))

        quit_text = font.render("Press 'Q' to quit", True, (255, 255, 255))
        sc.blit(quit_text, (W // 2 - quit_text.get_width() // 2, H // 2 + quit_text.get_height() * 2))

        pygame.display.update()
        clock.tick(60)

def show_win_screen():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        sc.fill((0, 0, 0))
        sc.blit(svitok2_image, (0, 0))
        font = pygame.font.SysFont('segoe print', 18)

        button_rect_text = font.render(("Конец!"), True, (255, 0, 0))
        sc.blit(button_rect_text, (W//2, H//2 + 200))

        button_width = 200
        button_height = 50
        button_x = W // 2 - button_width // 2
        button_y = H - 150
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.display.update()
        clock.tick(60)
    #if n == 6:
        #enB = pygame.sprite.groupcollide(enemies, bullet, False, True)
        #enb1=pygame.sprite.spritecollideany(hero_sprite, bullet_enemy)
        #enemies.update(hero_sprite, goblin_surf_right,goblin_surf_left,goblin_surf_up, goblin_surf_down, 10, sc, enB,enb1)
#enemies.update(hero_sprite, demon_surf_right,demon_surf_left,demon_surf_up, demon_surf_down, 10, sc, enB,enb1)
#if n == 6:
    #enemies_sprite_distant = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),
                                           #random.randint(var_h + 100, H - var_h - 100), goblin_surf_up[0], 100, 1)
    #enemies.add(enemies_sprite_distant)
portals = pygame.sprite.Group()
collide = False
time1 = pygame.time.get_ticks()


boss_timer_bullet=0
bullet_boss=pygame.sprite.Group()

bullet_enemy_1 = pygame.sprite.Group()

enemies_1 = pygame.sprite.Group()
enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), goblin_surf_up[0], 100, 3,5)
enemies_1.add(enemies_sprite_distant_1)

bullet_enemy_2 = pygame.sprite.Group()
enemies_2 = pygame.sprite.Group()
enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), demon_surf_up[0], 100, 2,7)
enemies_2.add(enemies_sprite_distant_2)


enemies_3 = pygame.sprite.Group()
enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), fire_surf_up[0], 100, 1,fire_attack_surf_right[0],10)
enemies_3.add(enemies_sprite)

boss = pygame.sprite.Group()


n=1
pause = False
running = False
settings_screen = False
death_screen = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if not running:
        if text_screen:
            show_text_screen()
            text_screen = False
        if settings_screen:
            sc.blit(ui_background_image, (0, 0))
            game_title_text = font.render("Legends of EVI", True, (255, 255, 255))
            sc.blit(game_title_text, (game_title_x, game_title_y))
        if pause:
            play_text = pause_text
        sc.blit(ui_background_image, (0, 0))
        game_title_text = font.render("Legends of EVI", True, (255, 255, 255))
        sc.blit(game_title_text, (game_title_x, game_title_y))
        sc.blit(play_cur, (play_button_x, play_button_y))
        sc.blit(settings_cur, (settings_button_x, settings_button_y))
        sc.blit(exit_cur, (exit_button_x, exit_button_y))
        if not pause:
            sc.blit(play_text, (play_button_x + 50, play_button_y + 20))
        else:
            sc.blit(play_text, (play_button_x + 20, play_button_y + 20))
        sc.blit(settings_text, (settings_button_x + 30, settings_button_y + 20))
        sc.blit(exit_text, (exit_button_x + 60, exit_button_y + 20))
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if play_button_x < mouse_pos[0] < play_button_x + button_width and \
                    play_button_y < mouse_pos[1] < play_button_y + button_height:
                if settings_screen:
                    settings_screen = False  # Если на экране настроек, то закрываем его
                else:
                    play_cur = play_button_image_pressed
                    running = True
                # Обработка нажатия на кнопку "Играть"
                print("Нажата кнопка Играть")
            elif settings_button_x < mouse_pos[0] < settings_button_x + button_width and \
                    settings_button_y < mouse_pos[1] < settings_button_y + button_height:
                # Обработка нажатия на кнопку "Настройки"
                settings_screen = True
                show_setting_screen()
                print("Нажата кнопка Настройки")

                settings_cur = settings_button_image_pressed
            elif exit_button_x < mouse_pos[0] < exit_button_x + button_width and \
                    exit_button_y < mouse_pos[1] < exit_button_y + button_height:
                # Обработка нажатия на кнопку "Выйти"
                if settings_screen:
                    settings_screen = False  # Если на экране настроек, то закрываем его
                else:
                    exit_cur = exit_button_image_pressed
                    exit()
        else:
            play_cur = play_button_image
            settings_cur = settings_button_image
            exit_cur = exit_button_image
    else:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            pause = True
        time1 = pygame.time.get_ticks()
        sc.blit(bg, (0, 0))

        if((len(enemies_1)+len(enemies_2)+len(enemies_3)==0 and len(boss)==0) or restart_game==True):
            portals = new_room_portal_update(room1.way1, room1.way2)
            if ((pygame.sprite.spritecollide(hero_sprite, portals, False, pygame.sprite.collide_circle)) or restart_game==True):
                if ((event.type == pygame.KEYDOWN) or  restart_game==True):
                    if ((event.key == pygame.K_RETURN) or  restart_game==True):
                        restart_game = False
                        schet+=1
                        room1.new_room(hero_sprite)
                        walls = new_room(room1.way1, room1.way2)
                        portals=new_room_portal(room1.way1, room1.way2)
                        n=random.randint(1,6)
                        print(schet)
                        if(schet<10):
                            if n == 1:
                                enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),goblin_surf_up[0], 100, 3, 5)
                                enemies_1.add(enemies_sprite_distant_1)
                                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                                enemies_2.add(enemies_sprite_distant_2)
                                enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), fire_surf_up[0],100, 1, fire_attack_surf_right[0], 10)
                                enemies_3.add(enemies_sprite)
                            if n == 2:
                                enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),goblin_surf_up[0], 100, 3, 5)
                                enemies_1.add(enemies_sprite_distant_1)
                                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                                enemies_2.add(enemies_sprite_distant_2)
                                enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), martin_surf_up[0],100, 1, martin_attack_surf_right[0], 10)
                                enemies_3.add(enemies_sprite)
                            if n == 3:
                                enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),goblin_surf_up[0], 100, 3, 5)
                                enemies_1.add(enemies_sprite_distant_1)
                                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                                enemies_2.add(enemies_sprite_distant_2)
                                enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),hashashin_surf_up[0], 100, 1, hashashin_attack_surf_right[0], 10)
                                enemies_3.add(enemies_sprite)
                            if n == 4:
                                enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),goblin_surf_up[0], 100, 3, 5)
                                enemies_1.add(enemies_sprite_distant_1)
                                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                                enemies_2.add(enemies_sprite_distant_2)
                                enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), ground_surf_up[0],100, 1, ground_attack_surf_right[0], 10)
                                enemies_3.add(enemies_sprite)
                            if n == 5:
                                enemies_sprite_distant_1 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),goblin_surf_up[0], 100, 3, 5)
                                enemies_1.add(enemies_sprite_distant_1)
                                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                                enemies_2.add(enemies_sprite_distant_2)
                                enemies_sprite = Enemy(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), water_surf_up[0],100, 1, water_attack_surf_right[0], 10)
                                enemies_3.add(enemies_sprite)
                        else:
                            boss_time = pygame.time.get_ticks()
                            boss_timer_bullet = pygame.time.get_ticks()
                            boss_sprite = Boss(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), boss_surf_up[0], 500,1, boss_attack_surf_right[0], 10)
                            boss.add(boss_sprite)
                            enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100),demon_surf_up[0], 100, 2, 7)
                            enemies_2.add(enemies_sprite_distant_2)

        if (hero_sprite.health <= 0):
            death_screen = True
            show_game_over_screen()
            schet = 0

        if (len(boss) == 0 and schet == 10):
            show_win_screen()

        if pygame.sprite.spritecollide(hero_sprite, walls, False, pygame.sprite.collide_circle):
            collide = True
        else:
            collide = False



        if (enemies_sprite_distant_2.prov_att):
            d=random.randint(1,8)
            bullet_enemy_2_timer = new_bullet_enemy_2(bullet_enemy_2_timer, time1, bullet_enemy_surf_up, bullet_enemy_2, d)

        if(schet==10):
            boss_update()
            if(len(enemies_2)==0 and boss_time<30000 and len(boss)==0):
                enemies_sprite_distant_2 = Enemy_Distant(random.randint(var_w + 100, W - var_w - 100),random.randint(var_h + 100, H - var_h - 100), demon_surf_up[0],100, 2, 7)
                enemies_2.add(enemies_sprite_distant_2)
                boss_time=0
        else:
            enemy_update(n)
            if (enemies_sprite_distant_1.prov_att):
                d = random.randint(1, 8)
                bullet_enemy_1_timer = new_bullet_enemy_1(bullet_enemy_1_timer, time1, green_bullet_enemy_surf_up,bullet_enemy_1, d)

            if (len(enemies_1) != 0):
                bullet_enemy_1.update()
            for bullets_enemy_1 in bullet_enemy_1.sprites():
                if bullets_enemy_1.rect.y < 0 or bullets_enemy_1.rect.y > H or bullets_enemy_1.rect.x < 0 or bullets_enemy_1.rect.x > W:
                    bullet_enemy_1.remove(bullets_enemy_1)
            pygame.sprite.groupcollide(bullet_enemy_1, walls, True, False)
            if (pygame.sprite.groupcollide(bullet_enemy_1, ghero, True, False)):
                hero_sprite.take_damage(enemies_sprite_distant_1.damage)
            if (len(enemies_1) != 0):
                for bullets_1 in bullet_enemy_1.sprites():
                    sc.blit(bullets_1.image, bullets_1.rect)

        hero_sprite.update(pygame.key.get_pressed(), room1.way1, room1.way2, collide, sc, hero_costumes)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_d]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_up_right, bullet, 5)
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_up_left, bullet, 6)
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_down_left, bullet, 7)
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_down_right, bullet, 8)
        elif keys[pygame.K_w]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_surf_up, bullet, 1)
        elif keys[pygame.K_s]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_surf_down, bullet, 2)
        elif keys[pygame.K_a]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_surf_left, bullet, 3)
        elif keys[pygame.K_d]:
            bullet_timer = new_bullet(bullet_timer, time1, bullet_surf_right, bullet, 4)
        bullet.update()

        if (len(enemies_2) != 0):
            bullet_enemy_2.update()
        for bullets in bullet.sprites():
            if bullets.rect.y < 0 or bullets.rect.y > H or bullets.rect.x < 0 or bullets.rect.x > W:
                bullet.remove(bullets)



        for bullets_enemy_2 in bullet_enemy_2.sprites():
            if bullets_enemy_2.rect.y < 0 or bullets_enemy_2.rect.y > H or bullets_enemy_2.rect.x < 0 or bullets_enemy_2.rect.x > W:
                bullet_enemy_2.remove(bullets_enemy_2)

        pygame.sprite.groupcollide(bullet_enemy_2, walls, True, False)
        if (pygame.sprite.groupcollide(bullet_enemy_2, ghero, True, False)):
            hero_sprite.take_damage(enemies_sprite_distant_2.damage)

        pygame.sprite.groupcollide(bullet, walls, True, False)

        walls.draw(sc)
        portals.draw(sc)
        for bullets in bullet.sprites():
            sc.blit(bullets.image, bullets.rect)

        if (len(enemies_2) != 0):
            for bullets_2 in bullet_enemy_2.sprites():
                sc.blit(bullets_2.image, bullets_2.rect)

        sc.blit(hero_sprite.image, hero_sprite.rect)



    clock.tick(FPS)
    pygame.display.update()

