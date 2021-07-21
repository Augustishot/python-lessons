import pygame
from sys import exit
pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption('My Game')

width = 800
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

s1 = pygame.Surface((100, 100))
s1.fill('darkgoldenrod')

s2 = pygame.Surface((50, 50))
s2.fill('gold')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill((0, 0, 0))
    
    screen.blit(s1, (400, 250))
    screen.blit(s2, (127, 100))
    
    pygame.display.update()
    clock.tick(60)