import pygame
import sys
import random

# --- CONFIGURATION ET LORE ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# Couleurs Thématiques
C_VOID = (10, 10, 15)      # Le vide d'Onyx
C_HERO = (0, 200, 255)     # L'éclat d'Ether
C_LORE = (240, 230, 200)   # Parchemin ancien

# Histoire : Valoria n'est plus que ruines. Malakor a dévoré le soleil. 
# Vous portez l'ultime étincelle. Chaque ennemi vaincu libère une bribe de mémoire.

class DialogueSystem:
    """Gère l'affichage narratif en bas de l'écran."""
    def __init__(self, font):
        self.font = font
        self.message = ""
        self.active = False

    def afficher(self, texte):
        self.message = texte
        self.active = True

    def draw(self, screen):
        if self.active:
            # Boite de dialogue
            rect = pygame.Rect(50, 450, 700, 120)
            pygame.draw.rect(screen, (20, 20, 30), rect)
            pygame.draw.rect(screen, C_LORE, rect, 2)
            
            # Rendu du texte (découpage simple)
            words = self.message.split(' ')
            line = ""
            y_offset = 470
            for word in words:
                test_line = line + word + " "
                if self.font.size(test_line)[0] < 660:
                    line = test_line
                else:
                    surf = self.font.render(line, True, C_LORE)
                    screen.blit(surf, (70, y_offset))
                    line = word + " "
                    y_offset += 25
            surf = self.font.render(line, True, C_LORE)
            screen.blit(surf, (70, y_offset))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(C_HERO)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hp = 100
        self.fragments_memoire = 0

    def update(self, keys, walls):
        dx, dy = 0, 0
        speed = 5
        if keys[pygame.K_z]: dy = -speed
        if keys[pygame.K_s]: dy = speed
        if keys[pygame.K_q]: dx = -speed
        if keys[pygame.K_d]: dx = speed

        # Logique de collision simplifiée
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, walls): self.rect.x -= dx
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, walls): self.rect.y -= dy

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, lore_msg):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.lore_msg = lore_msg

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Georgia", 20)
        self.dialogue = DialogueSystem(self.font)
        
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        self.setup_level()
        self.dialogue.afficher("Silas... Réveille-toi. Le sanctuaire est tombé. Retrouve les fragments de notre histoire avant que l'Onyx ne les efface.")

    def setup_level(self):
        # Création d'une arène de ruines
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                if x == 0 or x >= SCREEN_WIDTH-TILE_SIZE or y == 0 or y >= 400:
                    wall = pygame.sprite.Sprite()
                    wall.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
                    wall.image.fill((40, 40, 50))
                    wall.rect = wall.image.get_rect(topleft=(x, y))
                    self.walls.add(wall)
                    self.all_sprites.add(wall)

        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

        # Ennemis porteurs de Lore
        e1 = Enemy(400, 200, "FRAGMENT : 'L'an 402, Malakor offrit l'immortalité en échange de l'ombre.'")
        e2 = Enemy(600, 100, "FRAGMENT : 'Le Roi de Valoria fut le premier à boire le poison.'")
        self.enemies.add(e1, e2)
        self.all_sprites.add(e1, e2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN and self.dialogue.active:
                    self.dialogue.active = False # Ferme le dialogue

            if not self.dialogue.active:
                keys = pygame.key.get_pressed()
                self.player.update(keys, self.walls)

            # Interaction avec les ennemis (Combat & Lore)
            hit = pygame.sprite.spritecollideany(self.player, self.enemies)
            if hit:
                self.dialogue.afficher(hit.lore_msg)
                hit.kill()
                self.player.fragments_memoire += 1

            # Rendu
            self.screen.fill(C_VOID)
            self.all_sprites.draw(self.screen)
            
            # UI Info
            info = self.font.render(f"Fragments : {self.player.fragments_memoire}/2", True, C_LORE)
            self.screen.blit(info, (20, 20))
            
            self.dialogue.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    Game().run()