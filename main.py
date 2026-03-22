import pygame
import random

# button position variables for more readable code
# battle logic

class Battle:
    def __init__(self,battler1,battler2):
        self.battler1 = battler1
        self.battler2 = battler2
        battlers = [self.battler1, self.battler2]
    def course():
        while not ((self.battler2.aliveHeroes) or (self.battler1.aliveHeroes)):
            BattleTurn.checkSpeed((promptBattler()))

        

class BattleTurn:
    def checkSpeed():
        if (Battler1.currentHero.speed > Battler2.currentHero.speed):
            Battler1.currentHero.action()
            Battler2.currentHero.action()
        elif (Battler1.currentHero.speed < Battler2.currentHero.speed):
            Battler2.currentHero.action()
            Battler1.currentHero.action()
        else:
            random.choice(Battler1.currentHero.speed,Battler2.currentHero.speed)


class Player:
    def __init__(self, name, heroParty):
        self.name = name
        self.heroParty = []
        self.currentHeroIndex = 0
        self.aliveHeroes = 0

class Move:
    def __init__(self, name, damage, target):
        self.name = name
        self.damage = damage
        self.target = target
    
    def action():
        return Player.currentHero.health - Move.damage


def drawBattleUI():
    pygame.draw.rect(screen, (128, 128, 128), (10, 2*height//3, width-20, height//3 - 10), border_radius=10)
    drawSwitchButton()
    drawMoveButton()
    drawContractButton()
    drawArtifactsButton()

def drawSwitchButton():
    pygame.draw.rect(screen, (0,0,0), ((width-20)//2, (2*height//3)+height//24, width//4, height//8))
    if ((width-20)//2 <= pygame.mouse.get_pos()[0] <= (width-20)//2 + width//4 and
        (2*height//3)+height//24 <= pygame.mouse.get_pos()[1] <= (2*height//3)+height//24+height//8):
        print("inside")

def drawMoveButton():
    pygame.draw.rect(screen, (0,255,0), ((width-20)//2, (2*height//3)+(height//24*4), width//4, height//8))

def drawContractButton():
    pygame.draw.rect(screen, (0,0,255), (((width-20)//2)+width//4, (2*height//3)+(height//24), width//4, height//8))

def drawArtifactsButton():
    pygame.draw.rect(screen, (0,0,255), (((width-20)//2)+width//4, (2*height//3)+(height//24*4), width//4, height//8))

width,height = 800,600
#gameloop stuff
pygame.init()

gameClock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
    screen.fill((255,255,255))
    drawBattleUI()
    pygame.display.flip()
    gameClock.tick(60)

pygame.quit()
