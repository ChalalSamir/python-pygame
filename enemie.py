import math
import pygame

class Enemie:
    def __init__(self,ecran,x,y,direction,listEnemies):
        self.x = x
        self.y = y
        self.vit = 50
        self.dir = direction
        self.ecran = ecran
        self.listEnemies = listEnemies

    def Draw(self):
        pygame.draw.circle(self.ecran,(255,0,0),(self.x,self.y),20)
    def Update(self,deltatime):
        if self.dir == "right":
            self.x += deltatime* self.vit
        elif self.dir == "left":
            self.x -= deltatime* self.vit
        self.y += deltatime* 200
        self.Destroy()


    def Collision(self,player):
        x =  math.sqrt((player.x-self.x)**2+(player.y - self.y)**2)
        if x <= 40:
            pygame.quit()
        elif x <= 20 + player.shieldTaille:
            self.listEnemies.remove(self)

    def Destroy(self):
        if self.x<0 or self.y<0 or self.y > 1000 or self.x> 1000:
            self.listEnemies.remove(self)

            

    