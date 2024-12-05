import pygame
from src.Background import Background
from src.Monster import Monster
from src.Player import Player
import random

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        

    def run_game(self):
        clock = pygame.time.Clock()
        monsters = []
        player = Player(self.screen, 1)

        while True:
            #frame control
            clock.tick(120)

            #handle background
            background = Background(self.screen)
            background.run_background()

            #handle monster
            if random.random() < 0.05:  # 5% chance of spawning a new monster
                monster = Monster(self.screen, 1, 1280, random.randint(225, 570))
                monsters.append(monster)

            for monster in monsters:
                monster.run_monster()
                monster.rect.x -= 11  # move the monster to the left
                if monster.rect.x <= 0:  # remove the monster if it's off the screen
                    monsters.remove(monster)

            #handle player
            player.handle_input()
            player.run_player()

            pygame.display.flip()


            #handle close the game
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    exit()