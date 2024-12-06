import pygame
import random

class Monster:
    def __init__(self, screen, frame, move, spawn):
        self.screen = screen
        self.move = move
        self.image = pygame.image.load(f"assets/monster/slime{frame}.png")
        self.rect = self.image.get_rect(left=move, top=spawn)
        self.frame = frame
        self.mask = pygame.mask.from_surface(self.image)

    def run_monster(self):
        self.screen.blit(source=self.image, dest=self.rect)
        if self.frame < 8:
            self.frame += 1  # increment the frame attribute
        if self.frame == 8:
            self.frame = 1
        self.image = pygame.image.load(f"assets/monster/slime{self.frame}.png")  # update the image
        if self.frame > 8:
            self.image = pygame.transform.scale(self.image, (75, 15))
            self.rect.width = 0
            self.rect.height = 0
        else:
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect.width = 50
            self.rect.height = 50