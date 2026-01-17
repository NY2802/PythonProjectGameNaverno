import pygame
from pygame import *
from stegents import *
from pygame import *
from random import randint
init()
class Person:
    def __init__(self,name,speed,start,jump_power,full_health,image,weight,pos,health):
        self.name=name
        self.full_health=full_health
        self.speed=speed
        self.x=pos[0]
        self.y=pos[1]
        self.jump_power=jump_power
        self.health=health
        self.image=image
        self.wid,self.hei=image.get_size()
        self.power_in_jump=0
        self.weight=weight
        self.start =start
        self.savepos=self.start
    def go_left(self,blocks):
        self.x-=self.speed
        player=Rect(
            [self.x,self.y-5],
            [self.wid,self.hei]
        )
        for block in blocks:
            if player.colliderect(block):
                self.x += self.speed
    def go_right(self,blocks):
        self.x += self.speed
        player = Rect(
            [self.x, self.y-5],
            [self.wid, self.hei]
        )
        for block in blocks:
            if player.colliderect(block):
                self.x -= self.speed
    def jump(self,blocks):
        player = Rect(
            [self.x, self.y+5],
            [self.wid, self.hei]
        )
        for block in blocks:
            if player.colliderect(block):
                self.power_in_jump+=self.jump_power
        print(self.power_in_jump)
    def update(self,blocks):
        if self.health>self.full_health:
            self.health=self.full_health
        player = Rect(
            [self.x, self.y],
            [self.wid, self.hei]
        )
        for block in blocks:
            if player.colliderect(block):
                self.savepos=[self.x,self.y]
        keys=key.get_pressed()
        if keys[K_d]:
            self.go_right(blocks)
        if keys[K_a]:
            self.go_left(blocks)
        if keys[K_w]:
            self.jump(blocks)
        if self.power_in_jump==0:
            player = Rect(
                [self.x, self.y],
                [self.wid, self.hei]
            )
            a=True
            for block in blocks:
                if player.colliderect(block):
                    a=False
            if a:
                self.y+=self.weight
                if self.y>hei-self.hei:
                    self.x,self.y=self.savepos
                    self.health-=1
                if self.health<1:
                    self.x,self.y=self.start
                    self.health=self.full_health
        else:
            self.power_in_jump-=1
            self.y-=10
            for block in blocks:
                if player.colliderect(block):
                    self.y+=20
                    self.power_in_jump=0
    def draw(self,sc):
        draw.line(sc, (125, 125, 125), [hei / 2 - 100, 0], [hei / 2 - 100 + 550, 0],width=10)
        draw.line(sc,(255,0,0),[hei/2-100,0],[hei/2-100+(550/self.full_health*self.health),0],width=10)
        sc.blit(self.image,[self.x,self.y])
class Human(Person):
    def __init__(self):
        super().__init__("Human",3,[0,360],16,3,image.load("image\\human.png"),1,[0, 360],3)
class Cto_to_bistriy(Person):
    def __init__(self):
        super().__init__("Sonic",6, [0, 360], 11, 3, image.load("image\\Cto_to_bistriy.png"), 0.7,[0, 360],3)
class Cto_to_prig(Person):
    def __init__(self):
        super().__init__("Prusina",1.5, [0, 360], 36, 3, image.load("image\\Cto_to_prig.png"), 1,[0, 360],3)
class Gnom(Person):
    def __init__(self):
        super().__init__("Gnom",2.5, [0, 360], 11, 5, image.load("image\\Gnom.png"), 1.5,[0, 360],5)
