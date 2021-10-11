import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:
    def __init__(self, x = 0, y = 0, r = 10, vx = 0, vy = 0, color = BLUE):
        self.x = randint(100,700)
        self.y = randint(100,500)
        self.r = randint(10,30)
        self.vx = randint(-50, 50)
        self.vy = randint(-50, 50)
        self.color = COLORS[randint(0, 5)]
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

k = 0
number_of_balls = 13

balls = [Ball() for i in range(number_of_balls)]

t = -1

while not finished:
    clock.tick(FPS)
    t += 1
    for i in range(number_of_balls):
        if balls[i].x >= 1200 - balls[i].r or balls[i].x <= balls[i].r:
            balls[i].vx = -balls[i].vx
        elif balls[i].y >= 900 - balls[i].r or balls[i].y <= balls[i].r:
            balls[i].vy = -balls[i].vy
        balls[i].x = balls[i].x + balls[i].vx
        balls[i].y = balls[i].y + balls[i].vy
        balls[i].draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            x0 = ball.x
            y0 = ball.y
            r = ball.r
            d = (x - x0) ** 2 + (y - y0) ** 2
            if d < r ** 2:
                k = k + 1
    pygame.display.update()
    screen.fill(BLACK)

print(k)

pygame.quit()
