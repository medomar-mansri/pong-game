import pygame, sys
pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('ping pong')
ball = pygame.Rect(screen_width/2 - 15 ,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)
bg_color = pygame.Color('grey')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen,bg_color,player)
    pygame.draw.rect(screen,bg_color,opponent)
    pygame.draw.ellipse(screen,bg_color,ball) 
    pygame.draw.aaline(screen, bg_color, (screen_width/2, 0), (screen_width/2, screen_height))



    pygame.display.flip()
    clock.tick(60)