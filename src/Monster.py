import pygame
import random

class Monster:
    def __init__(self, screen, frame: int, move, spawn):
        self.screen = screen
        self.move = move
        self.image = pygame.image.load(f"assets/monster/slime{frame}.png")
        self.rect = self.image.get_rect(left=move, top=spawn)
        self.frame = frame

    def run_monster(self):
        self.screen.blit(source=self.image, dest=self.rect)
        self.frame += 1  # increment the frame attribute
        if self.frame >= 9:
            self.frame = 1
        self.image = pygame.image.load(f"assets/monster/slime{self.frame}.png")  # update the image
        self.image = pygame.transform.scale(self.image, (50, 50))