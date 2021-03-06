import math
from random import choice
from random import randint

import pygame


FPS = 50

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy += 1
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx = (-1) * self.vx
        if self.y >= 600 - self.r or self.y <= self.r:
            self.vy = (-1) * self.vy
        self.vy += 1
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            int(self.r)
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (self.r + obj.r) ** 2 + 1000:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5 * bullet
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            except:
                self.an = 90
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (20, 430, 20, 20)
        )
    def draw_targetting(self, event):
        pygame.draw.line(
            self.screen,
            BLACK,
            (20, 450), (event.pos[0], event.pos[1]), 2
        )
        print(event.pos[0], event.pos[1])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 5
            self.color = RED
        else:
            self.color = GREY


class Target:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(50, 70)
        self.live = 1
        self.points = 0
        self.color = RED

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(50, 70)
        self.live = 1
        self.color = RED
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (int(self.x), int(self.y)),
            int(self.r)
        )

class Bomb:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = 400
        self.y = 0
        self.v = 0
        self.r = randint(20, 50)

    def move(self):
        self.v += 1
        self.y += self.v

    def new_bomb(self):
        self.x = 400
        self.y = 0
        self.v = 0
        self.side = randint(20, 50)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            BLACK,
            (self.x - 0.5 * self.r, self.y - 0.5 * self.r, self.r, self.r)
        )
        


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
bomb = Bomb(screen)
finished = False

while not finished:
    clock.tick(FPS)

    screen.fill(WHITE)
    gun.draw()
    target.draw()
    bomb.draw()
    bomb.move()
    if bomb.y >= 580:
        bomb.new_bomb()
    for b in balls:
        b.draw()
    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if b.hittest(bomb):
            balls.remove(b)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun.draw_targetting(event)

    pygame.display.update()
    gun.power_up()

pygame.quit()
