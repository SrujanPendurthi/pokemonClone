import pygame
import random

class Battle:
    def __init__(self, battler1, battler2):
        self.battler1 = battler1
        self.battler2 = battler2

    def course(self):
        while self.battler1.aliveHeroes() and self.battler2.aliveHeroes():
            BattleTurn.checkSpeed(self.battler1, self.battler2)

class BattleTurn:
    def checkSpeed(battler1, battler2):
        if battler1.currentHero().speed > battler2.currentHero().speed:
            battler1.currentHero().action(battler2.currentHero())
            battler2.currentHero().action(battler1.currentHero())
        elif battler1.currentHero().speed < battler2.currentHero().speed:
            battler2.currentHero().action(battler1.currentHero())
            battler1.currentHero().action(battler2.currentHero())
        else:
            first, second = random.choice([
                (battler1, battler2),
                (battler2, battler1)
            ])
            first.currentHero().action(second.currentHero())
            second.currentHero().action(first.currentHero())

class Player:
    def __init__(self, name, heroParty):
        self.playerX, self.playerY = 200, 200
        self.name = name
        self.heroParty = heroParty
        self.currentHeroIndex = 0

    def currentHero(self):
        return self.heroParty[self.currentHeroIndex]

    def aliveHeroes(self):
        return any(hero.health > 0 for hero in self.heroParty)

    def switchHero(self, index):
        if 0 <= index < len(self.heroParty) and self.heroParty[index].health > 0:
            self.currentHeroIndex = index

class Hero:
    def __init__(self, name, health, attack, defense, speed):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = []

    def action(self, target):
        if self.moves:
            move = self.moves[0]
            move.apply(target)

    def isAlive(self):
        return self.health > 0

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def apply(self, target):
        actualDamage = max(0, self.damage - target.defense)
        target.health -= actualDamage
        print(f"{target.name} took {actualDamage} damage! {target.health} HP remaining.")


def drawBattleUI(game):
    pygame.draw.rect(game.screen, (128, 128, 128), (10, 2*game.height//3, game.width-20, game.height//3 - 10), border_radius=10)
    drawMoveButton(game)
    drawSwitchButton(game)
    drawContractButton(game)
    drawArtifactsButton(game)

def drawMoveButton(game):
    MoveButtonX, MoveButtonY = game.width - game.width//4*2 - 20, (2*game.height//3)+game.height//24
    MoveButtonW, MoveButtonH = game.width//4, game.height//8
    MoveButtonColor = (0, 0, 0)
    pygame.draw.rect(game.screen, MoveButtonColor, (MoveButtonX, MoveButtonY, MoveButtonW, MoveButtonH), border_radius=10)
    if (MoveButtonX <= pygame.mouse.get_pos()[0] <= MoveButtonX+MoveButtonW and
        MoveButtonY <= pygame.mouse.get_pos()[1] <= MoveButtonY+MoveButtonH and
        game.isMouseClicked):
        BattleTurn.checkSpeed(game.battle.battler1, game.battle.battler2)

def drawSwitchButton(game):
    SwitchButtonX, SwitchButtonY = game.width - game.width//4*2 - 20, (2*game.height//3)+(game.height//24*4)
    SwitchButtonW, SwitchButtonH = game.width//4, game.height//8
    SwitchButtonColor = (0, 255, 0)
    pygame.draw.rect(game.screen, SwitchButtonColor, (SwitchButtonX, SwitchButtonY, SwitchButtonW, SwitchButtonH), border_radius=10)
    if (SwitchButtonX <= pygame.mouse.get_pos()[0] <= SwitchButtonX+SwitchButtonW and
        SwitchButtonY <= pygame.mouse.get_pos()[1] <= SwitchButtonY+SwitchButtonH and
        game.isMouseClicked):
        print("click switch")

def drawContractButton(game):
    ContractButtonX, ContractButtonY = game.width - game.width//4 - 20, (2*game.height//3)+(game.height//24)
    ContractButtonW, ContractButtonH = game.width//4, game.height//8
    ContractButtonColor = (0, 0, 255)
    pygame.draw.rect(game.screen, ContractButtonColor, (ContractButtonX, ContractButtonY, ContractButtonW, ContractButtonH), border_radius=10)
    if (ContractButtonX <= pygame.mouse.get_pos()[0] <= ContractButtonX+ContractButtonW and
        ContractButtonY <= pygame.mouse.get_pos()[1] <= ContractButtonY+ContractButtonH and
        game.isMouseClicked):
        print("click Contract")

def drawArtifactsButton(game):
    ArtifactsButtonX, ArtifactsButtonY = game.width - game.width//4 - 20, (2*game.height//3)+(game.height//24*4)
    ArtifactsButtonW, ArtifactsButtonH = game.width//4, game.height//8
    ArtifactsButtonColor = (255, 0, 0)
    pygame.draw.rect(game.screen, ArtifactsButtonColor, (ArtifactsButtonX, ArtifactsButtonY, ArtifactsButtonW, ArtifactsButtonH), border_radius=10)
    if (ArtifactsButtonX <= pygame.mouse.get_pos()[0] <= ArtifactsButtonX+ArtifactsButtonW and
        ArtifactsButtonY <= pygame.mouse.get_pos()[1] <= ArtifactsButtonY+ArtifactsButtonH and
        game.isMouseClicked):
        print("click Artifacts")