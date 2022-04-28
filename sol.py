import pygame

from enemie import Enemie
from player import Perso
class Sol:
    def __init__(self,ecran,x,y,width,heigh):
        self.x = x
        self.y = y
        self.width = width
        self.heigh = heigh
        self.ecran = ecran

    def Draw(self):
        pygame.draw.rect(self.ecran, (0,255,0), pygame.Rect(self.x, self.y, self.width, self.heigh))

    def Collision(self, player):
        if self.y <= player.y +20 and player.x +20 >= self.x:
            if player.x -20 <= self.x+self.width and player.y-20<=self.y+self.heigh:
            #in
                x = self.x + self.width/2
                y = self.y + self.heigh/2
                if player.y>self.y and player.y<self.y+self.heigh:
                    if player.x< x:
                        player.x = self.x-20
                        if type(player) == Enemie:
                            player.dir = 'left'
                    if player.x > x:
                        if type(player) == Enemie:
                            player.dir = 'right'
                        player.x = self.x+self.width+20
                if player.x> self.x and player.x<self.x +self.width:
                    if player.y < y:
                        player.y = self.y - 20
                        if type(player) == Perso:
                            player.canjump = True
                    if player.y > y:
                        player.y = self.y+self.heigh +20
                        if type(player) == Perso:
                            player.sautForce = 0


