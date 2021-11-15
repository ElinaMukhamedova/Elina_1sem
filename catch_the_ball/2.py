import math
import json
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
    def __init__(self):
        self.x = randint(100,700)
        self.y = randint(100,500)
        self.r = randint(20,50)
        self.vx = randint(-20, 20)
        self.vy = randint(-20, 20)
        self.color = COLORS[randint(1, 5)]
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

class Red_Ball:
    def __init__(self):
        self.x = randint(100,700)
        self.y = randint(100,500)
        self.r = 60
        self.vx = randint(5, 10)
        self.vy = randint(5, 10)
        self.color = COLORS[0]
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

class Cube:
    def __init__(self):
        self.x = randint(10, 1100)
        self.y = randint(10, 800)
        self.d = randint(70, 100)
        self.color = COLORS[randint(0, 5)]
    def draw(self):
        rect(screen, self.color, (self.x, self.y, self.d, self.d))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

k_balls = 0
points_for_balls = 2
number_of_balls = randint(10, 20)
balls = [Ball() for i in range(number_of_balls)]

k_red_balls = 0
points_for_red_balls = 1
number_of_red_balls = randint(5, 10)
red_balls = [Red_Ball() for i in range(number_of_red_balls)]

k_cubes = 0
points_for_cubes = 3

data = {}

with open(r"rank.json") as f:
    data = json.load(f)

number_of_participants = len(data)
names = [""] * number_of_participants
i = 0
for key in data:
    names[i] = key
    i += 1
time_limit = 50
timer = 0

while not finished and timer <= time_limit * number_of_participants:
    clock.tick(FPS)
    timer += 1
    distsq = {}
    for i in range(number_of_red_balls):
        for j in range(number_of_red_balls):
            x1 = red_balls[i].x
            y1 = red_balls[i].y
            x2 = red_balls[j].x
            y2 = red_balls[j].y
            distsq[(i, j)] = (x1 - x2) ** 2 + (y1 - y2) ** 2

    for i in range(number_of_balls):
        if balls[i].x >= 1200 - balls[i].r or balls[i].x <= balls[i].r:
            balls[i].vx = -balls[i].vx
        elif balls[i].y >= 900 - balls[i].r or balls[i].y <= balls[i].r:
            balls[i].vy = -balls[i].vy
        balls[i].x = balls[i].x + balls[i].vx
        balls[i].y = balls[i].y + balls[i].vy
        balls[i].draw()

    #for i in range(number_of_red_balls):
        #if red_balls[i].x >= 1200 - red_balls[i].r or red_balls[i].x <= red_balls[i].r:
            #red_balls[i].vx = -red_balls[i].vx
        #elif red_balls[i].y >= 900 - red_balls[i].r or red_balls[i].y <= red_balls[i].r:
            #red_balls[i].vy = -red_balls[i].vy
        #red_balls[i].x = red_balls[i].x + red_balls[i].vx
        #red_balls[i].y = red_balls[i].y + red_balls[i].vy
        #red_balls[i].draw()

    for i in range(number_of_red_balls):
        for j in  range(number_of_red_balls):
            if 120 ** 2 - 1000 <= distsq[(i, j)] <= 120 ** 2 + 1000:
                x1 = red_balls[i].x
                y1 = red_balls[i].y
                x2 = red_balls[j].x
                y2 = red_balls[j].y
                vx1 = red_balls[i].vx
                vy1 = red_balls[i].vy
                v1 = math.sqrt(vx1 ** 2 + vy1 ** 2)
                vx2 = red_balls[j].vx
                vy2 = red_balls[j].vy
                v2 = math.sqrt(vx2 ** 2 + vy2 ** 2)
                new_vx1 = int(v1 * (x1 - x2) / 120)
                new_vy1 = int(v1 * (y1 - y2) / 120)
                new_vx2 = int(v2 * (x2 - x1) / 120)
                new_vy2 = int(v2 * (y2 - y1) / 120)
                red_balls[i].vx = new_vx1
                red_balls[i].vy = new_vy1
                red_balls[j].vx = new_vx2
                red_balls[j].vy = new_vy2
        if red_balls[i].x >= 1200 - red_balls[i].r or red_balls[i].x <= red_balls[i].r:
            red_balls[i].vx = -red_balls[i].vx
        elif red_balls[i].y >= 900 - red_balls[i].r or red_balls[i].y <= red_balls[i].r:
            red_balls[i].vy = -red_balls[i].vy
        red_balls[i].x = red_balls[i].x + red_balls[i].vx
        red_balls[i].y = red_balls[i].y + red_balls[i].vy
        red_balls[i].draw()
        #red_balls[j].x = red_balls[j].x + red_balls[j].vx
        #red_balls[j].y = red_balls[j].y + red_balls[j].vy
        #red_balls[j].draw()

    cube = Cube()
    cube.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if (cube.x <= x <= cube.x + cube.d) and (cube.y <= y <= cube.y + cube.d):
                k_cubes = k_cubes + 1
            for i in range(number_of_balls):
                x0 = balls[i].x
                y0 = balls[i].y
                r = balls[i].r
                d = (x - x0) ** 2 + (y - y0) ** 2
                if d < r ** 2:
                    k_balls = k_balls + 1
            for i in range(number_of_red_balls):
                x0 = red_balls[i].x
                y0 = red_balls[i].y
                r = red_balls[i].r
                d = (x - x0) ** 2 + (y - y0) ** 2
                if d < r ** 2:
                    k_red_balls = k_red_balls + 1

    pygame.display.update()
    screen.fill(BLACK)

    if timer % time_limit == 0:
        k_participant = timer // time_limit
        data[names[k_participant - 1]] = k_red_balls * points_for_red_balls + k_balls * points_for_balls + k_cubes * points_for_cubes
        print('red balls = ', k_red_balls, 'points for red balls = ', k_red_balls * points_for_red_balls)
        print('random balls = ', k_balls, 'points for random balls = ', k_balls * points_for_balls)
        print('cubes = ', k_cubes, 'points for cubes = ', k_cubes * points_for_cubes)

with open(r"rank.json", 'w') as f:
    json.dump(data, f)
pygame.quit()
