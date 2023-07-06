import pygame
from time import *
pygame.init()

clock = pygame.time.Clock()
fps = 60

width = 700
height = 672
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space_fighters")
pygame.display.set_icon(pygame.image.load("Actual_display_icon.png"))
background = pygame.image.load("planet_background.jpg")
background = pygame.transform.scale(background, (width, height))


rocket1_right = pygame.image.load("new__rocket2.png")
rocket1_right = pygame.transform.scale(rocket1_right, (150, 150))
rocket1_left = pygame.transform.flip(rocket1_right, True, False)
rect1 = rocket1_right.get_rect()
rect1.x = 100
rect1.y = 500
movement1_horizontal = 0
movement1_vertical = 0


#player2
rocket2_right = pygame.image.load("new__rocket.png")
rocket2_right = pygame.transform.scale(rocket2_right, (150, 150))
rocket2_left = pygame.transform.flip(rocket2_right, True, False)
rect2 = rocket2_right.get_rect()
rect2.x = 455
rect2.y = 500
movement2_horizontal = 0
movement2_vertical = 0


sprite1 = rocket1_right
sprite2 = rocket2_right


rect1.y += movement1_vertical
rect2.y += movement2_vertical




run = True
while run:
    clock.tick(fps)
    screen.blit(background, (0, 0))

    screen.blit(sprite1, rect1)
    screen.blit(sprite2, rect2)

    rect1.x += movement1_horizontal
    rect2.x += movement2_horizontal

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movement1_horizontal = 4
            if event.key == pygame.K_LEFT:
                movement1_horizontal = -4

            if event.key == pygame.K_d:
                movement2_horizontal = 4
            if event.key == pygame.K_a:
                movement2_horizontal = -4




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                movement1_horizontal = 0
            if event.key == pygame.K_d or event.key == pygame.K_a:
                movement2_horizontal = 0

        if movement1_horizontal == 4:
            sprite1 = rocket1_right
        if movement1_horizontal == -4:
            sprite1 = rocket1_left
        if movement2_horizontal == 4:
            sprite2 = rocket2_right
        if movement2_horizontal == -4:
            sprite2 = rocket2_left

    pygame.display.update()