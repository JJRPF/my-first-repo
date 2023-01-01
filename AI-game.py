import pygame
import sys
import random
import time

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#display
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Cookie Clicker')
clock = pygame.time.Clock()

#images
cookieImg = pygame.image.load('cookie.png')
cookieImg = pygame.transform.scale(cookieImg, (50,50))

#cookie clicker
cookieClicker = 0
cookieClickerPerSec = 1
cookieClickerPerSecCost = 10
cookieClickerPerSecCost2 = 50
cookieClickerPerSecCost3 = 100
cookieClickerPerSecCost4 = 150
cookieClickerPerSecCost5 = 200
cookieClickerPerSecCost