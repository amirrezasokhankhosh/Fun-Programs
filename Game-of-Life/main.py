import numpy as np
import time
import pygame
from pygame.locals import KEYDOWN, K_q
import sys


def play_game(board, screen):
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
                sys.exit()
        update_screen(board)
        draw_lines()
        pygame.display.update()
        time.sleep(.2)
        new_board = find_next_generation(board)
        board = np.copy(new_board)


def add_lives(num=3):
    row, col = board.shape
    choices = np.random.choice(np.arange(row * col), num)
    for choice in choices:
        board[choice // col, choice % col] = 1
    # board[0,:] = 1


def find_next_generation(board):
    new_board = np.copy(board)
    row, col = board.shape
    for i in range(row):
        for j in range(col):
            num_alive = get_num_alive(i, j, board)
            if new_board[i, j] == 1 and (num_alive > 3 or num_alive < 2):
                new_board[i, j] = 0
            elif new_board[i, j] == 0 and num_alive == 3:
                new_board[i, j] = 1
    return new_board


def get_num_alive(row, col, board):
    neighbours = find_neighbours(row, col, board)
    num_alive = 0
    for neighbour in neighbours:
        if int(neighbour) == 1:
            num_alive += 1
    return num_alive


def find_neighbours(i, j, arr):

    neighbors = []

    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
        # corners
        new_neighbors = []
        if i != 0:
            new_neighbors.append(arr[i - 1, j])  # top neighbor
        if j != len(arr[i]) - 1:
            new_neighbors.append(arr[i, j + 1])  # right neighbor
        if i != len(arr) - 1:
            new_neighbors.append(arr[i + 1, j])  # bottom neighbor
        if j != 0:
            new_neighbors.append(arr[i, j - 1])  # left neighbor
        if i != 0 and j != 0:
            new_neighbors.append(arr[i - 1, j - 1])
        if i != 0 and j != len(arr[i]) - 1:
            new_neighbors.append(arr[i - 1, j + 1])
        if i != len(arr) - 1 and j != 0:
            new_neighbors.append(arr[i + 1, j - 1])
        if i != len(arr) - 1 and j != len(arr[i]) - 1:
            new_neighbors.append(arr[i + 1, j + 1])

    else:
        # add neighbors
        new_neighbors = [
            arr[i - 1, j],  # top neighbor
            arr[i, j + 1],  # right neighbor
            arr[i + 1, j],  # bottom neighbor
            arr[i, j - 1],   # left neighbor
            arr[i - 1, j - 1],
            arr[i - 1, j + 1],
            arr[i + 1, j - 1],
            arr[i + 1, j + 1]
        ]

    return new_neighbors


def update_screen(board):
    row, col = board.shape
    size_w = WIDTH // col
    size_h = HEIGHT // row
    for i in range(row):
        for j in range(col):
            if board[i, j] == 1:
                screen.fill(BLACK, (j * size_w, i * size_h,
                                    (j + 1) * size_w, (i + 1) * size_h))
            else:
                screen.fill(WHITE, (j * size_w, i * size_h,
                                    (j + 1) * size_w, (i + 1) * size_h))


def draw_lines():
    for i in range(ROW - 1):
        pygame.draw.line(screen, WHITE, (0, (i + 1) * (HEIGHT // ROW)),
                         (WIDTH - 1, (i + 1) * (HEIGHT // ROW)))
    for j in range(COL - 1):
        pygame.draw.line(screen, WHITE, ((j + 1) * (WIDTH // COL),
                                         0), ((j + 1) * (WIDTH // COL), HEIGHT - 1))


WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ROW = 60
COL = 60
INITIAL_ALIVE = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
screen.fill(WHITE)
draw_lines()

board = np.zeros((ROW, COL), dtype=int)
add_lives(INITIAL_ALIVE)

play_game(board, screen)
