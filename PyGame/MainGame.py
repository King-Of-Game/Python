#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
from Roles import *
from sys import exit



# 配置
FRAME_RATE = 70      # 定义画面帧率
ANIMATE_CYCLE = 30   # 定义动画周期（帧数）
score = 0            # 记录分数
ticks = 0            # 图片刷新周期
ticks_enemy1 = 0
ticks_enemy1_down = 0
clock = pygame.time.Clock()  # 创建一个记录时间的对象

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 定义游戏屏幕大小
pygame.display.set_caption('飞机大战')  # 标题


# 载入游戏音乐素材
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('sound/game_over.wav')
bullet_sound.set_volume(0.3)  # 音量
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)
pygame.mixer.music.load('sound/game_music.wav')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)


# 载入背景图素材（先通过.load方法载入图片再对图片进行操作）
background_img = pygame.image.load('image/background.png')
game_over_img = pygame.image.load('image/gameover.png')
# 载入整体资源图片素材
shoot_img = pygame.image.load('image/shoot.png')

# 设置玩家图片
player_imgs = []
player_imgs.append(shoot_img.subsurface(pygame.Rect(0, 99, 102, 126)))   # 从图片左上角开始：x坐标，y坐标,宽，高
player_imgs.append(shoot_img.subsurface(pygame.Rect(165, 360, 102, 126)))

player_imgs.append(shoot_img.subsurface(pygame.Rect(165, 234, 102, 126)))  # 以下是玩家爆炸图片
player_imgs.append(shoot_img.subsurface(pygame.Rect(330, 624, 102, 126)))
player_imgs.append(shoot_img.subsurface(pygame.Rect(330, 498, 102, 126)))
player_imgs.append(shoot_img.subsurface(pygame.Rect(432, 624, 102, 126)))
player_pos = [200, 500]  # 玩家飞机在界面的初始位置

# 设置玩家子弹图片
bullet_img = shoot_img.subsurface(pygame.Rect(1004, 987, 9, 21))

# 设置一类敌机图片
enemy1_imgs = []
enemy1_imgs.append(shoot_img.subsurface(pygame.Rect(534, 612, 57, 43)))
enemy1_imgs.append(shoot_img.subsurface(pygame.Rect(267, 347, 57, 43)))  # 敌机爆炸图片区域
enemy1_imgs.append(shoot_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_imgs.append(shoot_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_imgs.append(shoot_img.subsurface(pygame.Rect(930, 697, 57, 43)))


# 创建各个对象
player = Player(player_imgs[0], player_pos)
enemy1_group = pygame.sprite.Group()
enemy1_down_group = pygame.sprite.Group()


while True:
    # 控制游戏最大帧率为60
    clock.tick(FRAME_RATE)

    # 绘制背景
    screen.blit(background_img, (0, 0))  # 从窗口的左上角开始放背景图片

    # 绘制玩家飞机
    screen.blit(player.image, player.rect)  # 对象在自己身上画图

    # 改变玩家飞机图片来制造动态效果
    if player.death == False:
        player.image = player_imgs[ticks // (ANIMATE_CYCLE // 2)]
        if ticks % 10 == 0:
            bullet_sound.play()
            player.shoot(bullet_img)
        player.bullets.update()
        player.bullets.draw(screen)
    else:
        pass

    # 绘制一类敌机
    if ticks_enemy1 % 40 == 0:
        enemy1 = Enemy(enemy1_imgs[0], [random.randint(0, SCREEN_WIDTH - enemy1_imgs[0].get_width()), -enemy1_imgs[0].get_height()])
        enemy1_group.add(enemy1)
    enemy1_group.update()  # 移动敌机
    enemy1_group.draw(screen)  # 把敌机绘制在画面上

    # 判断敌机和子弹碰撞
    enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group, player.bullets, True, True))
    # 遍历敌方爆炸组
    num = 1
    for enemy1_down in enemy1_down_group:
        screen.blit(enemy1_imgs[num], enemy1_down.rect)  # 对象在自己身上画图
        if ticks_enemy1_down % 10 == 0:
            if num <= 4:
                if num == 1:
                    enemy1_down_sound.play()
                num += 1
            else:
                enemy1_down_group.remove(enemy1_down)

























    # 键盘触发事件
    key_pressed = pygame.key.get_pressed()
    if player.death == False:
        if key_pressed[K_UP] or key_pressed[K_w]:
            player.moveUp()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            player.moveDown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            player.moveLeft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            player.moveRight()

    ticks += 1
    if ticks >= ANIMATE_CYCLE:
        ticks = 0

    ticks_enemy1 += 1
    if ticks_enemy1 >= 40:
        ticks_enemy1 = 0

    ticks_enemy1_down += 1
    if ticks_enemy1_down >= 10:
        ticks_enemy1_down = 0



    # 更新屏幕
    pygame.display.update()


    # 处理游戏退出
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()












