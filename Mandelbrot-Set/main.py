import sys
import pygame
from pygame import KEYDOWN, K_q


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


WIDTH, HEIGHT = 600, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Set")

for i in range(WIDTH):
    for j in range(HEIGHT):
        a = translate(i, 0, WIDTH - 1, -2, 2)
        b = translate(j, 0, HEIGHT - 1, -2, 2)
        ca, cb= a, b
        z = 0
        
        for n in range(100):
            try:
                aa = (a * a) - (b * b)
            except :
                print(n, a, b)
            bb = 2 * a * b
            a = aa + ca
            b = bb + cb
            if a + b > 20:
                break
        
        bright = translate(n, 0, 99, 0, 255)
        screen.set_at((i, j), (bright, bright, bright))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
    pygame.display.update()