import pygame

#battle classes
class Battle:
    def __init__(self):
        self.battler1 = None
        self.battler2 = None
    def checkSpeed(battler1.Avatar, battler2.Avatar):
        if (battler1.Avatar.speed > battler2.Avatar.speed):
            doMove(batter1.Avatar)
            doMove(battler2.Avatar)
        elif (battler1.Avatar.speed < battler2.Avatar.speed):
            doMove(batter2.Avatar)
            doMove(battler1.Avatar)
        else:
            
            

class Battler:
    def __init__(self):
        self.name = None
        self.avatars = []

class Avatar:
    def __init__(self):
        self.name = None
        self.type = None
        self.health = None
        self.attack = None
        self.specialAttack = None
        self.defense = None
        self.specialDefense = None
        self.speed = None
    def move(Avatar):
        checkSpeed()
        if moveType == self:
            doMove()
        elif moveType == damaging:
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
