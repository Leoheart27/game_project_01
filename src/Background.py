import pygame
from src import Game


class Background():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/background/game_background_2.png")
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect(left=0, top=0)

    def run_background(self):
        self.screen.blit(source=self.image, dest=self.rect)