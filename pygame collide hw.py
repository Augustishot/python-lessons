import pygame
from sys import exit
import random
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('My Game')

width = 800
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

ex_x = 0
ex_y = 0

c = random.randint(10, 790)

gh_y = 0

text_font = pygame.font.Font('INVASION2000.TTF', 50)

bg_surf = pygame.image.load('Background.jpeg').convert_alpha()
gh_surf = pygame.image.load('ghost.png').convert_alpha()
gh_rect = gh_surf.get_rect(midbottom = (c, 0))
va_surf = pygame.image.load('vampire.png').convert_alpha()
va_rect = va_surf.get_rect(midbottom = (400, 410))
ex_surf = pygame.image.load('explosion.png').convert_alpha()

text_surf = text_font.render("When they collide...", False, 'Black')
text2_surf = text_font.render("Boom!", False, 'Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if va_rect.right < pygame.mouse.get_pos()[0]:
                va_rect.right = va_rect.right + 2
            if va_rect.left > pygame.mouse.get_pos()[0]:
                va_rect.left = va_rect.left - 2
            
    screen.blit(bg_surf, (0, 0))
           
    gh_rect.bottom = gh_rect.bottom + 2
    
    if gh_rect.top >= 500:
        gh_rect = gh_surf.get_rect(midbottom = (c, 100))
        c = random.randint(10, 790)
        
    if va_rect.left >= 800:
        va_rect.left = 0
    
    if gh_rect.colliderect(va_rect):
        ex_x = gh_rect.left - 30
        ex_y = gh_rect.top - 15
        screen.blit(ex_surf, (ex_x, ex_y))
        screen.blit(text2_surf, (300, 100))
    else:
        screen.blit(text_surf, (150, 100))

    screen.blit(gh_surf, (gh_rect))
    screen.blit(va_surf, (va_rect))

    pygame.display.update()
    clock.tick(100)
