import pygame
import random

# Initialise
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Avoider")
player = pygame.image.load('startup.png')
pygame.display.set_icon(player)

playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 350
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('asteroid.png')
enemyX = random.randint(0,800)
enemyY = random.randint(32,60)
enemyX_change = 0.3
enemyY_change = 0.35

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0.6
bulletY_change = 0.6
bullet_state = "ready"

background = pygame.image.load('background.png')

def player(x,y):
    screen.blit(playerImg, (x, y))


def enemy(x,y):
    screen.blit(enemyImg, (x, y))


def fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change  =0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change  =0.3
            if event.key == pygame.K_w:
                fire(playerX,playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
               playerY_change = 0


    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
    elif enemyX >= 736:
        enemyX_change = -0.3

    enemyY += enemyY_change

    if enemyY <= 0:
        enemyY_change = 0.3
    elif enemyY >= 536:
        enemyY_change = -0.3

    if bullet_state is "fire":
        fire(playerX,playerY)
        bulletY -= bulletY_change
        

    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()