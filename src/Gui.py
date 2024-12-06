import pygame

class Gui:
    def __init__(self, screen, count):
        self.screen = screen
        self.count = count
    
    def run_gui(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        score_text = font.render("Score: " + str(self.count), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def plus_one(self):
        self.count += 1

    def reset(self):
        self.count = 0