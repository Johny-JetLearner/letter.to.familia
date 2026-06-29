import pygame
import time
screen=pygame.display.set_mode((1000,900))
image_1=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\images (1).jpeg")
image_2=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\images (2).jpeg")
image_44=pygame.transform.scale(image_1,(1000,900))
image_33=pygame.transform.scale(image_2,(1000,900))
while True:
    screen.blit(image_44,(0,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(image_33,(0,0))
    pygame.display.update()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()