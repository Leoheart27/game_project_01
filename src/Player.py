import pygame

class Player():
    def __init__(self, screen, frame):
        self.screen = screen
        self.frame = frame
        self.image = pygame.image.load(f"assets/player/player{frame}.png")
        self.rect = self.image.get_rect(left=50, top=300)

    def run_player(self):
        if self.frame >5:
            self.image = pygame.transform.scale(self.image, (200, 100))
        else:
            self.image = pygame.transform.scale(self.image, (80, 120))
        self.screen.blit(source=self.image, dest=self.rect)
        
    def move_player(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.move_player(-20, 0)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
        if keys[pygame.K_RIGHT] and self.rect.x < 1200:
            self.move_player(20, 0)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
        if keys[pygame.K_UP] and self.rect.y > 150:
            self.move_player(0, -20)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
        if keys[pygame.K_DOWN] and self.rect.y < 520:
            self.move_player(0, 20)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
        if keys[pygame.K_SPACE]:
            self.frame = 6
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")