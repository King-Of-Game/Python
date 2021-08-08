#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from random import randint
from sys import exit



# 子弹类
class Bullet(pygame.sprite.Sprite):
    # 两个参数分别对应：对象和对象的位置
    def __init__(self, bullet_img, bullet_pos):
        pygame.sprite.Sprite.__init__(self)  # ※父构造函数
        self.image = bullet_img              # ※加载图片和存储图片
        self.rect = self.image.get_rect()    # ※.get_rect()方法可以得到图片的宽度和高度以及移动位置
        self.rect.midbottom = bullet_pos     # ※精灵图片的位置
        self.speed = 8

    # 控制子弹移动
    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.kill()


# 敌人类
class Enemy(pygame.sprite.Sprite):
    # 两个参数分别对应：对象和对象的位置
    def __init__(self, enemy_img, enemy_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_pos
        self.speed = 2

        # 爆炸画面索引
        self.down_index = 0


    # 控制敌人移动
    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# 玩家类
class Hero(pygame.sprite.Sprite):
    # 两个参数分别对应：对象和对象的位置
    def __init__(self, hero_img, hero_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = hero_img  # 加载储存图片
        self.rect = self.image.get_rect()  # 图片大小
        self.rect.topleft = hero_pos  # 图片位置
        self.speed = 6
        self.death = False
        # 玩家爆炸图片索引
        self.down_index = 1
        # 玩家子弹的Group
        self.bullets1 = pygame.sprite.Group()

    # 控制射击行为
    def shoot(self, bullet1_img):
        bullet1 = Bullet(bullet1_img, self.rect.midtop)  # 在玩家类中实例化一个子弹对象，第二个参数是让子弹从飞机的头部开始射出
        self.bullets1.add(bullet1)  # 在子弹组中不断添加子弹对象

    # 控制飞机移动
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed




# 配置
SCREEN_WIDTH = 480   # 定义窗口的宽度
SCREEN_HEIGHT = 640  # 定义窗口的长度
FRAME_RATE = 70      # 定义画面帧率
ANIMATE_CYCLE = 30   # 定义动画周期（帧数）
score = 0            # 记录分数
ticks = 0            # 图片刷新周期
clock = pygame.time.Clock()  # 创建一个记录时间的对象





# 初始化游戏
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])  # 初始化一个用于显示的窗口
pygame.display.set_caption('打飞机')  # 设置窗口标题


# 载入游戏音乐****************************
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')               # 子弹射出声音
enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')     # 敌机坠毁声音
game_over_sound = pygame.mixer.Sound('sound/game_over.wav')         # 游戏结束声音
bullet_sound.set_volume(0.25)                                       # 设置游戏音量
enemy1_down_sound.set_volume(0.5)
game_over_sound.set_volume(0.5)
pygame.mixer.music.load('sound/game_music.wav')                     # 游戏背景音乐
pygame.mixer.music.play(-1,0.0)                                     # 音乐无限循环
pygame.mixer.music.set_volume(0.25)
# 载入游戏音乐****************************


# 添加图片素材****************************

background = pygame.image.load('image/background.png')  # 载入背景图
gameover = pygame.image.load('image/gameover.png')      # 载入游戏结束图
shoot_img = pygame.image.load('image/shoot.png')        # 载入所有的飞机模型图片

# Hero图片
hero_imgs = []
hero_imgs.append(shoot_img.subsurface(pygame.Rect(0, 99, 102, 126)))     # 从模型图片左上角开始裁剪：x坐标，y坐标,宽，高
hero_imgs.append(shoot_img.subsurface(pygame.Rect(165, 360, 102, 126)))

hero_imgs.append(shoot_img.subsurface(pygame.Rect(165, 234, 102, 126)))  # 玩家爆炸图片区域
hero_imgs.append(shoot_img.subsurface(pygame.Rect(330, 624, 102, 126)))
hero_imgs.append(shoot_img.subsurface(pygame.Rect(330, 498, 102, 126)))
hero_imgs.append(shoot_img.subsurface(pygame.Rect(432, 624, 102, 126)))
hero_pos = [200, 500]  # 玩家飞机在界面的初始位置

# 载入玩家射出的子弹图片
bullet1_img = shoot_img.subsurface(pygame.Rect(1004, 987, 9, 21))

# enemy1图片
enemy1_img = shoot_img.subsurface(pygame.Rect(534, 612, 57, 43))
enemy1_down_imgs = []
enemy1_down_imgs.append(shoot_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(shoot_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(shoot_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(shoot_img.subsurface(pygame.Rect(930, 697, 57, 43)))

# 添加图片素材****************************


# 创建各个对象：
hero = Hero(hero_imgs[0], hero_pos)  # 创建玩家

enemy1_group = pygame.sprite.Group()  # 创建一类敌机组
enemy1_down_group = pygame.sprite.Group()  # 创建一类击毁敌人组


# 事件循环（main loop）
while True:
    clock.tick(FRAME_RATE)  # 限制游戏最大帧率（framerate为70）

    # 绘制背景
    screen.blit(background, (0, 0))  # 从窗口的左上角开始放背景图片

    # 改变飞机图片来制造动画效果
    if hero.death == True:
        if ticks % (ANIMATE_CYCLE // 2) == 0:
            hero.down_index += 1
            hero.image = hero_imgs[hero.down_index]
        if hero.down_index == 5:
            break
    else:
        hero.image = hero_imgs[ticks // (ANIMATE_CYCLE // 2)]  # 周期结束切换图片
        # 玩家射击
        if ticks % 10 == 0:
            bullet_sound.play()
            hero.shoot(bullet1_img)
        hero.bullets1.update()  # 控制子弹移动
        hero.bullets1.draw(screen)  # 绘制子弹

    screen.blit(hero.image, hero.rect)  # 绘制玩家飞机



    # 产生一类敌机（ # 敌机出现的位置x轴随机，y轴位置固定在屏幕最上方）
    if ticks % 30 == 0:
        enemy = Enemy(enemy1_img, [randint(0, SCREEN_WIDTH - enemy1_img.get_width()), -enemy1_img.get_height()])
        enemy1_group.add(enemy)
    # 控制一类敌机移动
    enemy1_group.update()
    # 绘制一类敌机
    enemy1_group.draw(screen)

    # 检测敌机与子弹的碰撞：
    # 　groupcollide(group1, group2, dokill1, dokill2, collided=None) -> Sprite_dict
    # 　group1——精灵组1
    # 　group2——精灵组2
    # 　dokill1——是否杀死发生碰撞时group1中的精灵对象
    # 　dokill2——是否杀死发生碰撞时group2中的精灵对象
    # 　collided——可选参数，可自定义一个回调函数，参数为两个精灵对象，用于自定义两个精灵是否发生碰撞，返回bool值；若忽略此参数，则默认碰撞条件为两个精灵的rect发生重叠
    # 　返回一个包含所有group1中与group2发生碰撞的精灵字典（dict）
    enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group, hero.bullets1, True, True))

    # 遍历敌方一类飞机爆炸组
    for enemy1_down in enemy1_down_group:
        screen.blit(enemy1_down_imgs[enemy1_down.down_index], enemy1_down.rect)
        # 刷新频率
        if ticks % (ANIMATE_CYCLE//2) == 0:
            if enemy1_down.down_index < 3:
                if enemy1_down.down_index == 0:
                    enemy1_down_sound.play()
                    score += 100
                enemy1_down.down_index += 1
            else:
                enemy1_down_group.remove(enemy1_down)


    # 检测玩家与敌机的碰撞***********************
    enemy1_down_list = pygame.sprite.spritecollide(hero, enemy1_group, True)
    if len(enemy1_down_list) > 0:
        enemy1_down_group.add(enemy1_down_list)
        hero.death = True
        game_over_sound.play()
    # 检测玩家与敌机的碰撞***********************


    # 计算得分
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)


    # 监听键盘事件
    key_pressed = pygame.key.get_pressed()
    if hero.death == False:
        if key_pressed[K_w] or key_pressed[K_UP]:
            hero.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            hero.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            hero.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            hero.moveRight()


    ticks += 1
    if ticks >= ANIMATE_CYCLE:
        ticks = 0






    # 更新屏幕
    pygame.display.update()




    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        # 判断退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


font = pygame.font.Font(None, 48)
text = font.render('Score: ' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 100
screen.blit(text, text_rect)
screen.blit(gameover, (0, 0))
while True:
    pygame.display.update()
    # 处理游戏退出
    # 从消息队列中循环取
    for event in pygame.event.get():
        # 判断退出游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()






















