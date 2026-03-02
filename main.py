import pygame
import random

#battle classes
class Battle:
    def __init__(self):
        self.battler1 = None
        self.battler2 = None
    
    def checkSpeed(Battle.battler1.Hero, Battle.battler2.Hero):
        if (battler1.Hero.speed > battler2.Hero.speed):
            doMove(batter1.Hero)
            doMove(battler2.Hero)
        elif (battler1.Hero.speed < battler2.Hero.speed):
            doMove(batter2.Hero)
            doMove(battler1.Hero)
        else:
            if not random.randint(0,1):
                doMove(battler1.Hero)
                doMove(battler2.Hero)
            else:
                doMove(battler2.Hero)
                doMove(battler1.Hero)
            
class Move:
    def __init__(self):
        self.moveType = None
        self.moveName = None
        self.moveDamage = None
        self.isMoveSpecial = False
        
class Battler:
    def __init__(self):
        self.name = None
        self.heroes = []
    def doMove(self):
        moveType = "Internal"
        if moveType == damaging:
            moveTarget = "External"
        
class Hero:
    def __init__(self):
        self.name = None
        self.type = None
        self.health = None
        self.attack = None
        self.specialAttack = None
        self.defense = None
        self.specialDefense = None
        self.speed = None
    def move(Hero):
        doMove()


#gameloop stuff
pygame.init()

gameClock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        
    screen.fill((0,0,0))
    pygame.display.flip()
    gameClock.tick(60)

pygame.quit()
