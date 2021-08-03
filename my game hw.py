import pygame
from sys import exit
import time
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('Game Pixel')

width = 1280
height = 720

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

text_font = pygame.font.Font('INVASION2000.TTF', 100)

bg_surf = pygame.image.load('sky background.png').convert_alpha()
ru_surf = pygame.image.load('running man.png').convert_alpha()
ru_rect = ru_surf.get_rect(midtop = (1280, 510))
mo_surf = pygame.image.load('monster.png').convert_alpha()
mo_rect = mo_surf.get_rect(midtop = (0, 520))
fl_surf = pygame.image.load('flag.png').convert_alpha()

n = 2
n2 = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    tse = pygame.time.get_ticks()
    
    r = ru_rect.top
    
    mo_rect.left = mo_rect.left + n
    
    if event.type == pygame.KEYDOWN:        
        if event.key == pygame.K_LEFT:
            ru_rect.left = ru_rect.left - 2
        if event.key == pygame.K_RIGHT:
            ru_rect.right = ru_rect.right + 2
        if event.key == pygame.K_UP:
            ru_rect.top = ru_rect.top - 80
        if r != 510:
            pygame.time.wait(n2)
            ru_rect.top = ru_rect.top + 80
        
    if mo_rect.left >= 1280 and n < 10:
        n = n + 2
    
    if mo_rect.left >= 1280 and n2 > 1:
        n2 = n2 - 1
    
    if mo_rect.left >= 1280:
        mo_rect.left = 0
    
    screen.blit(bg_surf, (0, 0))
    screen.blit(ru_surf, ru_rect)
    screen.blit(mo_surf, mo_rect)
    screen.blit(fl_surf, (0, 470))
    
    if mo_rect.colliderect(ru_rect):
        print('You lose in', str(tse / 1000), 'seconds.')
        pygame.quit()
        exit()
        
    if ru_rect.left <= -30:
        print('You win in', str(tse / 1000), 'seconds.')
        pygame.quit()
        exit()
        
    
    pygame.display.update()
    clock.tick(100)