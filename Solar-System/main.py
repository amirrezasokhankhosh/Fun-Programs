import pygame
import numpy as np
from pygame.locals import KEYDOWN, K_q
from planet import Planet
import sys


def draw_planet(planet):
    radius = planet.radius
    color = planet.color
    pygame.draw.circle(screen, color, (planet.x, planet.y), radius)


def earase_planet(planet):
    radius = planet.radius
    pygame.draw.circle(screen, (0, 0, 0), (planet.x, planet.y), radius)


def update_angles():
    for planet in planets:
        planet.update_angle()


def update_locations():
    for planet in planets:
        planet.x = (WIDTH / 2) + planet.distance * np.cos(planet.angle)
        planet.y = (HEIGHT / 2) + planet.distance * np.sin(planet.angle)


def draw_circles():
    pygame.draw.circle(screen, (255, 255, 255),
                       (WIDTH / 2, HEIGHT / 2), 46.122, 1)
    pygame.draw.circle(screen, (255, 255, 255),
                       (WIDTH / 2, HEIGHT / 2), 108.85, 1)
    pygame.draw.circle(screen, (255, 255, 255),
                       (WIDTH / 2, HEIGHT / 2), 148.91, 1)
    pygame.draw.circle(screen, (255, 255, 255),
                       (WIDTH / 2, HEIGHT / 2), 243.42, 1)
    pygame.draw.circle(screen, (255, 255, 255),
                       (WIDTH / 2, HEIGHT / 2), 449.7, 1)


WIDTH, HEIGHT = 1200, 650
BLACK = (0, 0, 0)
EARTH_V = 7.2921150 * (10 ** -5) * np.pi

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")
screen.fill(BLACK)

planets = []
circles = []
planets.append(Planet('Sun', 696.340 / 25, 0,
               (255, 255, 0), 0, WIDTH / 2, HEIGHT / 2, 0))
planets.append(Planet('Mercury', 2.440 * 3, 46.122, (169, 169, 169),
               0, WIDTH / 2, (HEIGHT / 2) - 46.122, EARTH_V * 1.607))
planets.append(Planet('Venus', 3.760 * 3, 108.85, (139, 125, 130),
               0, WIDTH / 2, (HEIGHT / 2) - 108.85, EARTH_V * 1.175))
planets.append(Planet('Earth', 6.371 * 3, 148.91, (128, 96, 67),
               0, WIDTH / 2, (HEIGHT / 2) - 148.91, EARTH_V))
planets.append(Planet('Mars', 3.390 * 3, 243.42, (173, 98, 66),
               0, WIDTH / 2, (HEIGHT / 2) - 243.42, EARTH_V * 0.808))
planets.append(Planet('Jupiter', 69.911 / 2, 449.7, (227, 110, 75),
               0, WIDTH / 2, (HEIGHT / 2) - 449.7, EARTH_V * 0.438))
pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2), 46.122, 1)
pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2), 108.85, 1)
pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2), 148.91, 1)
pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2), 243.42, 1)
pygame.draw.circle(screen, (255, 255, 255), (WIDTH / 2, HEIGHT / 2), 449.7, 1)

for planet in planets:
    draw_planet(planet)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
    for planet in planets:
        earase_planet(planet)
    draw_circles()
    update_angles()
    update_locations()
    for planet in planets:
        draw_planet(planet)
    pygame.display.update()
