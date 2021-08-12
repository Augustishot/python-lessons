import pygame
from sys import exit
import random
pygame.init()

clock = pygame.time.Clock()

time = 6
minust = False

width = 800
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

count = True

ex_x = 0
ex_y = 0

c = random.randint(10, 790)

gh_y = 0

score = 0
get_score = False

text_font = pygame.font.Font('INVASION2000.TTF', 50)
text_font2 = pygame.font.Font('INVASION2000.TTF', 25)
text_font3 = pygame.font.Font('invasion2000.ttf', 75)

bg_surf = pygame.image.load('Background.jpeg').convert_alpha()
gh_surf = pygame.image.load('ghost.png').convert_alpha()
gh_rect = gh_surf.get_rect(midbottom = (c, 0))
va_surf = pygame.image.load('vampire.png').convert_alpha()
va_rect = va_surf.get_rect(midbottom = (400, 410))
ex_surf = pygame.image.load('explosion.png').convert_alpha()
bg2_surf = pygame.image.load('endmenu.jpeg').convert_alpha()

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

def sb(font, size, word, tf, color):
    text_font2 = pygame.font.Font(font, size)
    text3_surf = text_font2.render(word, tf, color)
    screen.blit(text3_surf, (0, 0))

def tb(font, size, word, tf, color):
    text_font2 = pygame.font.Font(font, size)
    text4_surf = text_font2.render(word, tf, color)
    screen.blit(text4_surf, (450, 0))

while count == True:
    text5_surf = text_font3.render(str(time), False, 'Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if time > 0:
        pygame.time.delay(1000)
        time = time - 1
    else:
        pygame.time.delay(500)
        count = False
        
    screen.blit(bg2_surf, (0, 0))
    screen.blit(text5_surf, (400, 200))
    
    pygame.display.update()
    clock.tick(100)

while True and count == False:
    tse = pygame.time.get_ticks()
    pos2 = pos
    tse = int(tse / 1000 - 7)
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
    
    if gh_rect.colliderect(va_rect) and get_score == False:
        old_score = score
        score = score + 1
        get_score = True
        
    if get_score == True and not gh_rect.colliderect(va_rect):
        get_score = False

    screen.blit(gh_surf, (gh_rect))
    screen.blit(va_surf, (va_rect))
    sb('invasion2000.ttf', 30, "score : " + str(score), False, 'Black')
    tb('invasion2000.ttf', 30, "time : " + str(tse) + " seconds", False, 'Black')

    pygame.display.update()
    clock.tick(100)