#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, bullet_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = bullet_pos
        self.speed = 8

    def update(self):
        self.rect.top -= self.speed  # 使子弹向上移动


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, player_img, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.topleft = player_pos
        self.speed = 8
        self.death = False
        # 子弹组
        self.bullets = pygame.sprite.Group()

    def shoot(self,bullet_img):
        bullet = Bullet(bullet_img,self.rect.midtop)
        self.bullets.add(bullet)

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


# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = enemy_pos
        self.speed = 2
        self.death = False


    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

