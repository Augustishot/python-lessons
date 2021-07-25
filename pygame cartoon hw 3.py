import pygame
from sys import exit
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('My Game')

width = 800
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

text_font = pygame.font.Font('INVASION2000.TTF', 50)

bg_surf = pygame.image.load('Background.jpeg').convert_alpha()
gh_surf = pygame.image.load('ghost.png').convert_alpha()
br0_surf = pygame.image.load('brickwall_0.png').convert_alpha()
br1_surf = pygame.image.load('brickwall_1.png').convert_alpha()
br2_surf = pygame.image.load('brickwall_2.png').convert_alpha()
br3_surf = pygame.image.load('brickwall_3.png').convert_alpha()
fl_surf = pygame.image.load('flower.png').convert_alpha()
wi_surf = pygame.image.load('wizard.png').convert_alpha()
va_surf = pygame.image.load('vampire.png').convert_alpha()
pi_surf = pygame.image.load('pickle 2.png').convert_alpha()
text_surf = text_font.render("Let's Fly!", False, 'Black')

pi_x = 0
pi_y = 350
br0_x = 100
br1_x = 300
br2_x = 500
br3_x = 700
fl_y = 350
wi_y = 350
gh_y = 350
va_y = 350

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pi_x = pi_x + 2

    if pi_x >= 800:
        pi_x = 0
        pi_x = 0
    
    if pi_x == br0_x:
        fl_y = fl_y - 20
        
    if pi_x == br1_x:
        wi_y = wi_y - 20
        
    if pi_x == br2_x:
        gh_y = gh_y - 20
        
    if pi_x == br3_x:
        va_y = va_y - 20
    
    if fl_y <= 0:
        fl_y = 350
        
    if wi_y <= 0:
        wi_y = 350
        
    if gh_y <= 0:
        gh_y = 350
        
    if va_y <= 0:
        va_y = 350
    
    screen.blit(bg_surf, (0, 0))
    screen.blit(fl_surf, (100, fl_y))
    screen.blit(gh_surf, (500, gh_y))
    screen.blit(text_surf, (250, 30))
    screen.blit(wi_surf, (300, wi_y))
    screen.blit(va_surf, (700, va_y))
    screen.blit(br0_surf, (100, 350))
    screen.blit(br1_surf, (300, 350))
    screen.blit(br2_surf, (500, 350))
    screen.blit(br3_surf, (700, 350))
    screen.blit(pi_surf, (pi_x, pi_y))
    
    pygame.display.update()
    clock.tick(100)