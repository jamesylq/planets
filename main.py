import math
import pygame


def Threedigit(s: str):
    if len(s) == 1:
        return '00' + s
    if len(s) == 2:
        return '0' + s
    return s


screen = pygame.display.set_mode((700, 700))
pygame.init()
pygame.font.init()
pygame.display.set_caption('Solar System')
font = pygame.font.SysFont('comicsansms', 30)

speed = 0.05
cC = math.pi / 180
earthPerspective = False

MercuryDeg = 0
VenusDeg = 0
EarthDeg = 0
MoonDeg = 0
MarsDeg = 0
JupiterDeg = 0
UranusDeg = 0
NeptuneDeg = 0

SunColor = (255, 0, 0)
MercuryColor = (200, 200, 200)
VenusColor = (218, 193, 124)
EarthColor = (0, 128, 0)
MoonColor = (128, 128, 128)
MarsColor = (255, 64, 64)
JupiterColor = (201, 144, 57)
UranusColor = (147, 205, 241)
NeptuneColor = (62, 84, 232)
zoom = 1

cx = 0
cy = 0

while True:
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT]:
        cx += 1 / 4
    if keysPressed[pygame.K_RIGHT]:
        cx -= 1 / 4
    if keysPressed[pygame.K_UP]:
        cy += 1 / 4
    if keysPressed[pygame.K_DOWN]:
        cy -= 1 / 4

    if keysPressed[pygame.K_a]:
        zoom = max(0.05, zoom - 0.001)
    if keysPressed[pygame.K_d]:
        zoom = min(4, zoom + 0.001)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if earthPerspective:
                    cx, cy = 0, 0
                earthPerspective = not earthPerspective

    if earthPerspective:
        cx = -200 * math.sin(EarthDeg * cC) * zoom
        cy = -200 * math.cos(EarthDeg * cC) * zoom

    screen.fill(0)

    MercuryDeg += 365 / 88 * speed
    VenusDeg += 365 / 225 * speed
    MoonDeg += 365 / 27 * speed
    EarthDeg += speed
    MarsDeg += 365 / 687 * speed
    JupiterDeg += speed / 5
    UranusDeg += speed / 84
    NeptuneDeg += speed / 165

    # Sun
    pygame.draw.circle(screen, SunColor, (350 + cx, 350 + cy), 50 * zoom)
    # Mercury
    pygame.draw.circle(screen, MercuryColor, (350 + 80 * math.sin(MercuryDeg * cC) * zoom + cx,
                                              350 + 80 * math.cos(MercuryDeg * cC) * zoom + cy), 3.8 * zoom)
    # Venus
    pygame.draw.circle(screen, VenusColor, (350 + 140 * math.sin(VenusDeg * cC) * zoom + cx,
                                            350 + 140 * math.cos(VenusDeg * cC) * zoom + cy), 9.4 * zoom)
    # Earth
    pygame.draw.circle(screen, EarthColor, (350 + 200 * math.sin(EarthDeg * cC) * zoom + cx,
                                            350 + 200 * math.cos(EarthDeg * cC) * zoom + cy), 10 * zoom)
    # Moon
    pygame.draw.circle(screen, MoonColor,
                       (350 + 200 * math.sin(EarthDeg * cC) * zoom + 14 * math.sin(MoonDeg * cC) * zoom + cx,
                        350 + 200 * math.cos(EarthDeg * cC) * zoom + 14 * math.cos(MoonDeg * cC) * zoom + cy),
                       2.7 * zoom)
    # Mars
    pygame.draw.circle(screen, MarsColor, (350 + 304 * math.sin(MarsDeg * cC) * zoom + cx,
                                           350 + 304 * math.cos(MarsDeg * cC) * zoom + cy), 5.3 * zoom)
    # Jupiter
    pygame.draw.circle(screen, JupiterColor, (350 + 1000 * math.sin(JupiterDeg * cC) * zoom + cx,
                                              350 + 1000 * math.cos(JupiterDeg * cC) * zoom + cy), 42 * zoom)
    # Uranus
    pygame.draw.circle(screen, UranusColor, (350 + 4000 * math.sin(UranusDeg * cC) * zoom + cx,
                                             350 + 4000 * math.cos(UranusDeg * cC) * zoom + cy), 24.9 * zoom)
    # Neptune
    pygame.draw.circle(screen, NeptuneColor, (350 + 6000 * math.sin(NeptuneDeg * cC) * zoom + cx,
                                              350 + 6000 * math.cos(NeptuneDeg * cC) * zoom + cy), 24 * zoom)

    screen.blit(font.render(f'Zoom: {round(zoom, 2)}x', True, (255, 255, 255)), (10, 10))

    pygame.display.update()
