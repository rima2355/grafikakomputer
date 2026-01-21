import pygame
import random
import sys

pygame.init()

# Layar
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Tembak 2D")

clock = pygame.time.Clock()
FPS = 60

# Load gambar
player_img = pygame.image.load("player.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()
bullet_img = pygame.image.load("bullet.png").convert_alpha()
bg_img = pygame.image.load("background.png").convert()

player_img = pygame.transform.scale(player_img, (60, 60))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# Player
player_rect = player_img.get_rect(midbottom=(WIDTH//2, HEIGHT - 20))
player_speed = 6

# Bullet
bullets = []
bullet_speed = 10

# Enemy
enemies = []
enemy_speed = 3

def spawn_enemy():
    rect = enemy_img.get_rect(
        topleft=(random.randint(0, WIDTH - 50), random.randint(-150, -50))
    )
    enemies.append(rect)

for _ in range(4):
    spawn_enemy()

# Score & lives
score = 0
lives = 3
font = pygame.font.SysFont("arial", 24)

# Cooldown tembakan
shoot_delay = 300
last_shot = pygame.time.get_ticks()

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Gerak player
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed

    # Nembak
    now = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and now - last_shot > shoot_delay:
        bullet = bullet_img.get_rect(midbottom=player_rect.midtop)
        bullets.append(bullet)
        last_shot = now

    # Gerak peluru
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Gerak musuh
    for enemy in enemies[:]:
        enemy.y += enemy_speed

        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            spawn_enemy()
            lives -= 1

        # Tabrakan player
        if enemy.colliderect(player_rect):
            lives -= 1
            enemies.remove(enemy)
            spawn_enemy()

        # Tabrakan peluru
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                spawn_enemy()
                score += 10
                break

    # Game Over
    if lives <= 0:
        screen.fill((0, 0, 0))
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (WIDTH//2 - 80, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    # Render
    screen.blit(bg_img, (0, 0))
    screen.blit(player_img, player_rect)

    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    for enemy in enemies:
        screen.blit(enemy_img, enemy)

    # UI
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Lives: {lives}", True, (255, 255, 255)), (10, 40))

    pygame.display.update()
