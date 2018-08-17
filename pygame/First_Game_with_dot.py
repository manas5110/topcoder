import pygame
pygame.init()

win = pygame.display.set_mode((1200,600))

pygame.display.set_caption("First Python Game")


x=1000
y=30
width=10
height=10
velocity=5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=velocity
    if keys[pygame.K_RIGHT]:
        x+= velocity
    if keys[pygame.K_UP]:
        y-= velocity
    if keys[pygame.K_DOWN]:
        y+=velocity
    if x>1190:
        x=1190
    if y>590:
        y=590
    if x<0:
        x=0
    if y<0:
        y=0
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,255,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()