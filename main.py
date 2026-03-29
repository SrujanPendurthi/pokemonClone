import pygame
import random
from battle import *

def movement(player, game):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.playerY -= 5
    if keys[pygame.K_s]:
        player.playerY += 5
    if keys[pygame.K_a]:
        player.playerX -= 5
    if keys[pygame.K_d]:
        player.playerX += 5

class Game:
    def __init__(self):
        self.width, self.height = 800, 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.gameClock = pygame.time.Clock()
        self.isRunning = True
        self.isMouseClicked = False
        self.isBattleMode = False

        fireblast = Move("Fire Blast", 50)
        slash = Move("Slash", 30)

        hero1 = Hero("Pyro", 100, 40, 10, 8)
        hero1.moves.append(fireblast)

        hero2 = Hero("Knight", 120, 30, 20, 5)
        hero2.moves.append(slash)

        self.player1 = Player("Ash", [hero1])
        self.player2 = Player("Gary", [hero2])

        self.battle = Battle(self.player1, self.player2)

    def run(self):
        while self.isRunning:
            self.isMouseClicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.isMouseClicked = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.isBattleMode = not self.isBattleMode

            self.screen.fill((255, 255, 255))
            if not self.isBattleMode:
                movement(self.player1, self)
                pygame.draw.rect(self.screen, (255, 0, 0), (self.player1.playerX, self.player1.playerY, 50, 50))
            if self.isBattleMode:
                drawBattleUI(self)
            pygame.display.flip()
            self.gameClock.tick(60)

        pygame.quit()

game = Game()
game.run()