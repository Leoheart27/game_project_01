import pygame

class Player():
    def __init__(self, screen, frame):
        self.screen = screen
        self.frame = frame
        self.image = pygame.image.load(f"assets/player/player{frame}.png")
        self.rect = self.image.get_rect(left=50, top=300)
        self.attack = False
        self.attack_time = 0

    def run_player(self):
        if self.frame >5:
            self.image = pygame.transform.scale(self.image, (180, 90))
            self.rect.width = 180
            self.rect.height = 90
        else:
            self.image = pygame.transform.scale(self.image, (60, 100))
            self.rect.width = 40
            self.rect.height = 80
        self.screen.blit(source=self.image, dest=self.rect)
        self.mask = pygame.mask.from_surface(self.image)
        
    def move_player(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def get_rect(self):
        return self.rect
    
    def get_attack(self):
        return self.attack
    
    def attack_sfx(self, sfx):
        sfx.play()

    def handle_input(self, sfx):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.move_player(-25, 0)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")

        if keys[pygame.K_RIGHT] and self.rect.x < 1200:
            self.move_player(25, 0)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")

        if keys[pygame.K_UP] and self.rect.y > 150:
            self.move_player(0, -25)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")

        if keys[pygame.K_DOWN] and self.rect.y < 520:
            self.move_player(0, 25)
            if self.frame >= 5:
                self.frame = 1
            self.frame += 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")

        if keys[pygame.K_SPACE]:
            self.frame = 6
            self.attack = True
            self.attack_time = pygame.time.get_ticks()
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
            self.attack_sfx(sfx)

        if self.attack and pygame.time.get_ticks() - self.attack_time >= 400:
            self.attack = False
            self.frame = 1
            self.image = pygame.image.load(f"assets/player/player{self.frame}.png")
            self.rect.width = 40
            self.rect.height = 80