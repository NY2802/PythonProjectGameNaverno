import pygame
from pygame import *
from stegents import *
from persons import *
init()
sc=display.set_mode((wid,hei))
display.set_caption("GAME")
clock=time.Clock()
clock.tick(60)
menu=True
buttonplay=Rect([wid/2-100,hei/2-100],[250,100])
persons=[Human(),Cto_to_bistriy(),Cto_to_prig(),Gnom()]
person=0
font=font.Font(None,100)
while menu:
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
            exit()
        if event.type==MOUSEBUTTONDOWN:
            if buttonplay.collidepoint(mouse.get_pos()):
                menu=False
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                person-=1
                if person<0:
                    person=len(persons)-1
            if event.key==K_RIGHT:
                person+=1
                if person>len(persons)-1:
                    person=0
        sc.fill((255,255,255))
        sc.blit(persons[person].image,[wid/2,hei/2])
        draw.rect(sc,(0,0,255),buttonplay)
        sc.blit(font.render("   Play",True,(0,0,0)),[wid/2-100,hei/2-100])
        sc.blit(font.render("NAME: "+str(persons[person].name)+"\nSPEED: "+str(persons[person].speed)+"\nHEALTH: "+str(persons[person].health),True,(0,0,0)),[wid/2-100,hei/2+120])
        display.flip()
personn=persons[person]
blocks=[[0,500],[90,500],[90,450],[90,400],[90,350],[90,300],[90,250],[90,200],[90,150],[0,150],[40,150],[40,700],[90,700],[1000,680]]
blocks2=[]
for i in blocks:
    blocks2.append(Rect(i,[50,50]))
print(type(sc))
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                person -= 1
                if person < 0:
                    person = len(persons) - 1
            if event.key == K_RIGHT:
                person += 1
                if person > len(persons) - 1:
                    person = 0
            q=personn
            personn=persons[person]
            personn.health=q.health
            personn.x = q.x
            personn.y = q.y
            for block in blocks2:
                while True:
                    if Rect([personn.x,personn.y],[personn.wid,personn.hei]).colliderect(block):
                        personn.y-=1
                    else:
                        break
    sc.fill((255,255,255))
    personn.update(blocks2)
    personn.draw(sc)
    for block in blocks2:
        draw.rect(sc,(0,0,0),block)
    display.flip()
