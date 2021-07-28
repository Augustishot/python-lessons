import pygame
from sys import exit
import random
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Running man')

width = 800
height = 400

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

text_font = pygame.font.Font('INVASION2000.TTF', 50)

bg_surf = pygame.image.load('background2.jpeg').convert_alpha()
ru_surf = pygame.image.load('running.png').convert_alpha()
br_surf = pygame.image.load('wall.png').convert_alpha()
fl_surf = pygame.image.load('spike.png').convert_alpha
text_surf = text_font.render("Running Man", False, 'Black')

ru_x = 0
ru_y = 320
br_x = random.randint(100, 700)

while br_x / 2 != 0:
    br_x = br_x + 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    ru_x = ru_x + 2
    
    if ru_x >= 800:
        ru_x = 0
        br_x = random.randint(100, 700)

    if ru_x + 80 == br_x:
        ru_y = ru_y - 70
    
    if ru_x - 80 == br_x:
        ru_y = ru_y + 70

    screen.blit(bg_surf, (0, 0))
    screen.blit(ru_surf, (ru_x, ru_y))
    screen.blit(br_surf, (br_x, 330))
    screen.blit(text_surf, (400, 100))
    
    pygame.display.update()
    clock.tick(2000)