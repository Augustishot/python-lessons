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

score = 0
get_score = False

text_font = pygame.font.Font('INVASION2000.TTF', 50)
text_font2 = pygame.font.Font('INVASION2000.TTF', 25)

bg_surf = pygame.image.load('Background.jpeg').convert_alpha()
gh_surf = pygame.image.load('ghost.png').convert_alpha()
gh_rect = gh_surf.get_rect(midbottom = (c, 0))
va_surf = pygame.image.load('vampire.png').convert_alpha()
va_rect = va_surf.get_rect(midbottom = (400, 410))
ex_surf = pygame.image.load('explosion.png').convert_alpha()

text_surf = text_font.render("When they collide...", False, 'Black')
text2_surf = text_font.render("Boom!", False, 'Red')

pos = pygame.mouse.get_pos()[0]
pos2 = pygame.mouse.get_pos()[0]

n = 2
n2 = 1
speed = False

def move(n, pos, pos2):
    if pos < pos2:
        va_rect.left = va_rect.left - n
    if pos > pos2:
        va_rect.right = va_rect.right + n

def su(n):
    n = n + 0.05
    return n

def ss():
    n = 2
    return n

while True:
    pos2 = pos
    tse = pygame.time.get_ticks()
    tse = int(tse / 1000)
    pos = pygame.mouse.get_pos()[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Score :', str(score))
            print('Time :', str(tse))
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                n = su(n)
                move(n, pos, pos2)
            else:
                n = ss()
                move(n, pos, pos2)   
    
    text3_surf = text_font2.render("score : " + str(score), False, 'Violet')
    text4_surf = text_font2.render("time : " + str(tse) + " seconds", False, 'Violet')
    
    if n2 == 1:
        pos2 = pygame.mouse.get_pos()[0] + 0.01
        n2 = n2 + 1
    else:
        pos2 = pygame.mouse.get_pos()[0]
    
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
    
    if gh_rect.colliderect(va_rect) and get_score == False:
        old_score = score
        score = score + 1
        get_score = True
        
    if get_score == True and not gh_rect.colliderect(va_rect):
        get_score = False

    screen.blit(gh_surf, (gh_rect))
    screen.blit(va_surf, (va_rect))
    screen.blit(text3_surf, (0, 0))
    screen.blit(text4_surf, (0, 20))

    pygame.display.update()
    clock.tick(100)