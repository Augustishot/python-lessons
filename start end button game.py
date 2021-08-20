import pygame
from sys import exit
import random
pygame.init()

clock = pygame.time.Clock()

start = False
close = False
t = 30
time2 = 5
minust = False

b2 = 0
wait = False 

count = True

width = 800
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
end = False

ex_x = 0
ex_y = 0

c = random.randint(10, 790)

gh_y = 0

score = 0
get_score = False

text_font = pygame.font.Font('invasion2000.ttf', 50)
text2_font = pygame.font.Font('invasion2000.ttf', 30)


bg_surf = pygame.image.load('Background.jpeg').convert_alpha()
gh_surf = pygame.image.load('ghost.png').convert_alpha()
gh_rect = gh_surf.get_rect(midbottom = (c, 0))
va_surf = pygame.image.load('vampire.png').convert_alpha()
va_rect = va_surf.get_rect(midbottom = (400, 410))
ex_surf = pygame.image.load('explosion.png').convert_alpha()
start_surf2 = text2_font.render("start", False, 'White')
end_surf2 = text2_font.render("end", False, 'white')
bg2_surf = pygame.image.load('startmenu.jpeg').convert_alpha()
bg3_surf = pygame.image.load('endmenu.jpeg').convert_alpha()

pos = pygame.mouse.get_pos()[0]
pos2 = pygame.mouse.get_pos()[0]

n = 2
n2 = 1
n3 = 1
speed = False

def move(n, pos, pos2):
    if pos < pos2 and va_rect.left > 0:
        va_rect.left = va_rect.left - n
    if pos > pos2 and va_rect.right < 800:
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
    time3 = pygame.time.get_ticks()
    time3 = int(time3 / 1000)
    text5_surf = text2_font.render('press the button below to play', False, 'Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if start == False:
            position = pygame.mouse.get_pos()
            if (position[0] >= 336 and position[0] <= 464) and (position[1] >= 286 and position[1] <= 314):
                if pygame.mouse.get_pressed()[0]:
                    start = True
        else:
            count = False
        
    screen.blit(bg2_surf, (0, 0))
    screen.blit(text5_surf, (100, 200))
    pygame.draw.rect(pygame.display.set_mode((800, 500)), 'Black', pygame.Rect(336, 286, 128, 28))
    screen.blit(start_surf2, (356, 280))
    
    pygame.display.update()
    clock.tick(100)

while True and count == False and t > 0 and end == False:
    pos2 = pos
    pos = pygame.mouse.get_pos()[0]
    before = pygame.time.get_ticks()
    before = int(before / 1000 - time3)
    before = before - time3
    if before > b2:
        t = t - 1
        b2 = before
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    
    if n3 == 1:
        b2 = -1
        n3 = 2
    
    screen.blit(bg_surf, (0, 0))
           
    gh_rect.bottom = gh_rect.bottom + 2
    
    if gh_rect.top >= 500:
        gh_rect = gh_surf.get_rect(midbottom = (c, 100))
        c = random.randint(10, 790)
    
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
    
    if t == 0:
        end = True
    
    screen.blit(gh_surf, (gh_rect))
    screen.blit(va_surf, (va_rect))
    sb('invasion2000.ttf', 30, "score : " + str(score), False, 'Black')
    tb('invasion2000.ttf', 30, "time : " + str(t) + " seconds", False, 'Black')

    pygame.display.update()
    clock.tick(100)

while end == True:
    text6_surf = text_font.render("Score : " + str(score), False, 'Black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(bg3_surf, (0, 0))
    screen.blit(text6_surf, (250, 175))
    pygame.draw.rect(pygame.display.set_mode((800, 500)), 'Black', pygame.Rect(336, 286, 128, 28))
    screen.blit(end_surf2, (366, 280))
    
    if close == False:
        position = pygame.mouse.get_pos()
        if (position[0] >= 336 and position[0] <= 464) and (position[1] >= 286 and position[1] <= 314):
            if pygame.mouse.get_pressed()[0]:
                close = True
    else:
        pygame.quit()
        exit()
        
    pygame.display.update()
    clock.tick(100)