import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

def tree(x, y, a, b):
    rect(screen, (150, 75, 0), (x + a / 4, y + b, a / 2, 3 * b / 2))
    ellipse(screen, (34, 139, 34), (x, y + b, a, b))
    ellipse(screen, (34, 139, 34), (x, y, a, b))
    circle(screen, (34, 139, 34), (x + a / 2, y + b), 3 * a / 4)
    circle(screen, (255, 127, 127), (x + a, y + b), a / 5)
    circle(screen, (255, 127, 127), (x + a / 4, y + 2 * b / 5), a / 4)

def horse(x,y, a, b):
    ellipse(screen, (255, 255, 255), (x, y, a, b))
    rect(screen, (255, 255, 255), (x + a / 9, y + b / 2, a / 9, 3 * b / 2))
    rect(screen, (255, 255, 255), (x + 3 * a / 9, y + b / 4, a / 9, 3 * b / 2))
    rect(screen, (255, 255, 255), (x + 5 * a / 9, y + b / 2, a / 9, 3 * b / 2))
    rect(screen, (255, 255, 255), (x + 7 * a / 9, y + b / 4, a / 9, 3 * b / 2))
    ellipse(screen, (255, 255, 255), (x + 7 * a / 9, y - b, 2 * a / 9, 3 * b / 2))
    ellipse(screen, (255, 255, 255), (x + 7 * a / 9, y - 5 * b / 6, 4 * a / 9, b / 3))
    circle(screen, (255, 255, 255), (x + 8 * a / 9, y - 5 * b / 6), 2 * a / 9)
    circle(screen, (0, 50, 255), (x + a, y - 5 * b / 6), a / 15)
    circle(screen, (0, 0, 0), (x + a, y - 5 * b / 6), a / 30)
    polygon(screen, (106, 90, 205), [(x + 8 * a / 9, y - 5 * b / 3), (x + a,y - b), (x + 7 * a / 9,y - b)])
    ellipse(screen, (0, 191, 255), (x + 5.5 * a / 9, y - 5 * b / 4, 4 * a / 9, b / 3))
    ellipse(screen, (30, 144, 235), (x + 4.5 * a / 9, y - 4 * b / 4, 4 * a / 9, b / 3))
    ellipse(screen, (0, 0, 128), (x + 4 * a / 9, y - 3 * b / 4, 5 * a / 9, b / 2))
    ellipse(screen, (138, 43, 226), (x + 3 * a / 9, y - 0.35 * b, 5 * a / 9, b / 2))
    circle(screen, (123, 104, 238), (x, y + b / 2), 2 * a / 9)
    ellipse(screen, (0, 0, 139), (x - 3 * a / 9, y + 0.5 * b, 5 * a / 9, b / 2))
    ellipse(screen, (138, 43, 226), (x - 3.5 * a / 9, y + 0.8 * b, 5 * a / 9, b / 2))
    ellipse(screen, (25, 25, 112), (x - 4 * a / 9, y + 1.1 * b, 5 * a / 9, b / 2))
    ellipse(screen, (75, 0, 130), (x - 4 * a / 9, y + 1.4 * b, 5 * a / 9, b / 2))


rect(screen, (135, 206, 250), (0, 0, 400, 270))
rect(screen, (0, 255, 0), (0, 270, 400, 330))
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                               (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
circle(screen, (255, 200, 0), (380, 50), 70)
tree(0, 150, 60, 75)
tree(70, 160, 50, 100)
tree(30, 350, 70, 90)

horse(200, 300, 100, 70)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
