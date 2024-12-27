import pygame

class Score:
    def __init__(self, screen, count, position: tuple):
        self.screen = screen
        self.count = count
        self.position = position
    
    def run_score(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        score_text = font.render("Score: " + str(self.count), True, (255, 255, 255))
        self.screen.blit(score_text, self.position)

    def plus_one(self):
        self.count += 1

    def reset(self):
        self.count = 0