import pygame
from enemie import Enemie 
from player import Perso
import random
from sol import Sol

pygame.init()
timerEnemy = 2
ecran = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("oklm")

p  = Perso(ecran)
solList = []
enemies=[]
fallSpeed = 0
pause = 0

solList.append(Sol(ecran,0,700,1000,50))
solList.append(Sol(ecran,500,640,50,60))
solList.append(Sol(ecran,100,500,200,60))

list = ["left", "right"]
		
for i in range(0):
    solList.append(Sol(ecran,random.randint(0, 1000),random.randint(0, 700),random.randint(40, 200),random.randint(40, 200)))
for i in range(0):
    enemies.append(Enemie(ecran, random.randint(0, 1000), random.randint(0, 500), random.choice(list), enemies))

loop = True
getTicksLastFrame = 0

while loop:
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    timerEnemy -= deltaTime
    if timerEnemy<=0:
        timerEnemy = 2
        enemies.append(Enemie(ecran, random.randint(0, 1000), random.randint(0, 500), random.choice(list), enemies))

    p.Update(deltaTime)

    for sol in solList:
        sol.Collision(p)
        for en in enemies:
            sol.Collision(en)

    for en in enemies:
        en.Collision(p)
        en.Update(deltaTime)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                if p.canjump:
                    p.canjump = False
                    p.sautForce = p.maxSautForce
            if event.key == pygame.K_p:
                if not p.shieldActive:
                    p.shieldActive = True
        if event.type == pygame.QUIT:
            loop = False
    ecran.fill((0,0,0))
    
    for sol in solList:
        sol.Draw()
    p.Draw()

    for en in enemies:
        en.Draw()
    pygame.display.flip()

 
pygame.quit()