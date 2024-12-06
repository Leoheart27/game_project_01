import pygame
from src.Background import Background
from src.Monster import Monster
from src.Player import Player
from src.Gui import Gui
from assets.sfx import *
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        

    def run_game(self):
        clock = pygame.time.Clock()
        monsters = []
        player = Player(self.screen, 1)
        pygame.mixer.init()
        score = 0
        gui_score = Gui(self.screen, score)

        #sfx
        sweep = pygame.mixer.Sound("assets/sfx/sweep.wav")
        splash = pygame.mixer.Sound("assets/sfx/splash.wav")
        forest = pygame.mixer.Sound("assets/sfx/forest.wav")
        game1 = pygame.mixer.Sound("assets/sfx/game1.mp3")
        game1.play(-1)
        forest.play(-1)

        while True:
            #frame control
            clock.tick(120)


            #handle music

            #handle background
            background = Background(self.screen)
            background.run_background()

            #handle counters
            gui_score.run_gui()

            #handle player
            player.run_player()
            player.handle_input(sweep)
            player.get_attack()
            player_rect = player.get_rect()

            #handle monster
            if random.random() < 0.1:  # 10% chance of spawning a new monster
                monster = Monster(self.screen, 1, 1280, random.randint(225, 570))
                monsters.append(monster)

            for monster in monsters:
                monster.run_monster()
                monster.rect.x -= 12  # move the monster to the left
                if monster.rect.x <= 0:  # remove the monster if it's off the screen
                    monsters.remove(monster)

                #handle collision
                if player.rect.colliderect(monster.rect) and player.attack == True:
                    splash.play()
                    monster.frame = 9
                if monster.frame < 14 and monster.frame > 8:
                    monster.frame += 1
                if monster.frame == 13:
                    monsters.remove(monster)
                    gui_score.plus_one()
                if player.rect.colliderect(monster.rect) and player.attack == False:
                    player.rect.x = 50
                    player.rect.y = 300
                    self.screen.fill((0, 0, 0))



            pygame.display.flip()


            #handle close the game
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    exit()