import pygame
from time import sleep

pygame.init()


window= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(0.5)
image = pygame.image.load('scary.jpg')
window.blit(image, (350,200))
pygame.display.update()
sleep(3)
