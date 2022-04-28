import pygame
class Perso:
    def __init__(self,ecran):
        self.x = 300
        self.y = 500
        self.vit = 200
        self.ecran = ecran
        self.canjump = True
        self.sautForce = 0
        self.maxSautForce = 700
        self.shieldTaille = 0
        self.shieldActive = False
        self.timerShield = 0

    def Draw(self):
        pygame.draw.circle(self.ecran, (0,100,100), (self.x,self.y), self.shieldTaille)
        pygame.draw.circle(self.ecran, (0,0,255), (self.x,self.y), 20)
    def Update(self,deltatime):
        if pygame.key.get_pressed()[pygame.K_d]:
                self.x += deltatime * self.vit
        if pygame.key.get_pressed()[pygame.K_q]:
                self.x += -deltatime * self.vit               
        self.y += deltatime* 200
        self.jump(deltatime)
        self.Destroy()
        self.Shield(deltatime)
        
    def jump(self,deltatime):
        self.y -= deltatime* self.sautForce
        self.sautForce -= deltatime * 500
        if self.sautForce< 0 : self.sautForce = 0
    def Destroy(self):
        if self.x<0 or self.y<0 or self.y > 1000 or self.x> 1000:
            pygame.quit()
    def Shield(self,deltaTime):
        if self.shieldActive == True:
            self.timerShield += deltaTime
            if self.shieldTaille != -1:
                self.shieldTaille += deltaTime * 50
            if self.shieldTaille > 50:
                self.shieldTaille = -1
            if self.timerShield > 5:
                self.shieldActive = False
                self.timerShield = 0
                self.shieldTaille = 0



        

