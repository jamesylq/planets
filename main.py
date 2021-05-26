import math
import pygame
import random


screen = pygame.display.set_mode((800, 600))
pygame.init()


class gravityObj:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.mass = m
        self.color = random.randint(0, 0xFFFFFF)
        self.angle = random.randint(0, 360) / 180 * math.pi

        self.nx = x
        self.ny = y

    def move(self):
        self.nx += math.cos(self.angle) / 100
        self.ny += math.sin(self.angle) / 100
        for obj in gravityObjs:
            if obj != self:
                motion = getMotion(self, obj)
                self.nx += motion[0]
                self.ny += motion[1]

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

    def checkCollide(self):
        global gravityObjs

        for obj in gravityObjs:
            if obj != self:
                if math.sqrt(abs(obj.x - self.x) ** 2 + abs(obj.y - self.y) ** 2) < 5:
                    gravityObjs.remove(obj)
                    self.mass += obj.mass


def getMotion(a: gravityObj, b: gravityObj):
    """F = G * m1 * m2 / r^2"""
    dx = a.x - b.x
    dy = a.y - b.y
    hyp = math.sqrt(dx ** 2 + dy ** 2)

    Amx = 0
    Amy = 0

    if hyp >= 1:
        Amx = dx / hyp ** 3 * 50
        Amy = dy / hyp ** 3 * 50
    elif hyp > 0:
        Amx = dx * 50
        Amy = dy * 50

    return -Amx, -Amy


def move():
    for obj in gravityObjs:
        obj.move()
    for obj in gravityObjs:
        obj.x = obj.nx
        obj.y = obj.ny
    for obj in gravityObjs:
        obj.checkCollide()


def draw():
    screen.fill(0)
    for obj in gravityObjs:
        obj.draw()
    pygame.display.update()


gravityObjs = []
for n in range(100):
    gravityObjs.append(gravityObj(random.randint(0, 800), random.randint(0, 600), random.randint(100, 5000)))

while True:
    move()
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
