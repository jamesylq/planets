import math
import pygame

screen = pygame.display.set_mode((700, 700))
pygame.init()
pygame.font.init()
pygame.display.set_caption('Solar System')
font = pygame.font.SysFont('comicsansms', 30)
clock = pygame.time.Clock()

speed = 0.1
cC = math.pi / 180
earthPerspective = False
zoomFactor = 0.02
scrollFactor = 5 / 4

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

SunPoints = []
MercuryPoints = []
VenusPoints = []
EarthPoints = []
MoonPoints = []
MarsPoints = []
JupiterPoints = []
UranusPoints = []
NeptunePoints = []

zoom = 1

cx = 0
cy = 0


def draw(x):
    if earthPerspective:
        x.pop(3)
    else:
        x.pop(0)

    for l in x:
        for p in range(len(l) - 1):
            pygame.draw.line(screen, (255, 255, 255), l[p], l[p+1], 3)


def clear():
    global SunPoints, MercuryPoints, VenusPoints, EarthPoints, MoonPoints, MarsPoints, JupiterPoints, UranusPoints, NeptunePoints

    SunPoints = []
    MercuryPoints = []
    VenusPoints = []
    EarthPoints = []
    MoonPoints = []
    MarsPoints = []
    JupiterPoints = []
    UranusPoints = []
    NeptunePoints = []


while True:
    clock.tick(200)

    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT]:
        cx += scrollFactor
        clear()
    if keysPressed[pygame.K_RIGHT]:
        cx -= scrollFactor
        clear()
    if keysPressed[pygame.K_UP]:
        cy += scrollFactor
        clear()
    if keysPressed[pygame.K_DOWN]:
        cy -= scrollFactor
        clear()

    if keysPressed[pygame.K_a] and zoom - zoomFactor >= 0.05:
        cx *= (zoom - zoomFactor) / zoom
        cy *= (zoom - zoomFactor) / zoom
        zoom -= zoomFactor
        clear()
    if keysPressed[pygame.K_d] and zoom + zoomFactor <= 4:
        cx *= (zoom + zoomFactor) / zoom
        cy *= (zoom + zoomFactor) / zoom
        zoom += zoomFactor
        clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if earthPerspective:
                    cx, cy = 0, 0
                earthPerspective = not earthPerspective
                clear()

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
    SunPoints.append((350 + cx, 350 + cy))
    pygame.draw.circle(screen, SunColor, SunPoints[-1], 50 * zoom)
    # Mercury
    MercuryPoints.append((350 + 80 * math.sin(MercuryDeg * cC) * zoom + cx,
                          350 + 80 * math.cos(MercuryDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, MercuryColor, MercuryPoints[-1], 3.8 * zoom)
    # Venus
    VenusPoints.append((350 + 140 * math.sin(VenusDeg * cC) * zoom + cx,
                        350 + 140 * math.cos(VenusDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, VenusColor, VenusPoints[-1], 9.4 * zoom)
    # Earth
    EarthPoints.append((350 + 200 * math.sin(EarthDeg * cC) * zoom + cx,
                        350 + 200 * math.cos(EarthDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, EarthColor, EarthPoints[-1], 10 * zoom)
    # Moon
    MoonPoints.append((350 + 200 * math.sin(EarthDeg * cC) * zoom + 14 * math.sin(MoonDeg * cC) * zoom + cx,
                       350 + 200 * math.cos(EarthDeg * cC) * zoom + 14 * math.cos(MoonDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, MoonColor, MoonPoints[-1], 2.7 * zoom)
    # Mars
    MarsPoints.append((350 + 304 * math.sin(MarsDeg * cC) * zoom + cx,
                       350 + 304 * math.cos(MarsDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, MarsColor, MarsPoints[-1], 5.3 * zoom)
    # Jupiter
    JupiterPoints.append((350 + 1000 * math.sin(JupiterDeg * cC) * zoom + cx,
                          350 + 1000 * math.cos(JupiterDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, JupiterColor, JupiterPoints[-1], 42 * zoom)
    # Uranus
    UranusPoints.append((350 + 4000 * math.sin(UranusDeg * cC) * zoom + cx,
                         350 + 4000 * math.cos(UranusDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, UranusColor, UranusPoints[-1], 24.9 * zoom)
    # Neptune
    NeptunePoints.append((350 + 6000 * math.sin(NeptuneDeg * cC) * zoom + cx,
                          350 + 6000 * math.cos(NeptuneDeg * cC) * zoom + cy))
    pygame.draw.circle(screen, NeptuneColor, NeptunePoints[-1], 24 * zoom)

    if len(SunPoints) > 250:
        SunPoints.pop(0)
        MercuryPoints.pop(0)
        VenusPoints.pop(0)
        EarthPoints.pop(0)
        MoonPoints.pop(0)
        MarsPoints.pop(0)
        JupiterPoints.pop(0)
        UranusPoints.pop(0)
        NeptunePoints.pop(0)

    if keysPressed[pygame.K_m]:
        draw([SunPoints, MercuryPoints, VenusPoints, EarthPoints, MoonPoints, MarsPoints, JupiterPoints, UranusPoints, NeptunePoints])

    screen.blit(font.render(f'Zoom: {round(zoom, 2)}x', True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f'{round(clock.get_fps())} FPS', True, (255, 255, 255)), (10, 40))

    pygame.draw.line(screen, (255, 255, 255), (345, 350), (355, 350))
    pygame.draw.line(screen, (255, 255, 255), (350, 345), (350, 355))

    pygame.display.update()
