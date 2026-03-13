import pygame
from grid import *
from astar import astar

pygame.init()

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Visualization")


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main():

    grid = make_grid(ROWS, WIDTH)

    start = None
    goal = None

    running = True

    while running:

        draw(WIN, grid, ROWS, WIDTH)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if not start and node != goal:
                    start = node
                    start.make_start()

                elif not goal and node != start:
                    goal = node
                    goal.make_goal()

                elif node != start and node != goal:
                    node.make_wall()

            # RIGHT CLICK (remove node)
            elif pygame.mouse.get_pressed()[2]:

                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                node = grid[row][col]
                node.color = WHITE

                if node == start:
                    start = None
                elif node == goal:
                    goal = None

            # PRESS SPACE → RUN A*
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE and start and goal:
                    astar(lambda: draw(WIN, grid, ROWS, WIDTH),
                          grid, start, goal)

                # PRESS C → CLEAR GRID
                if event.key == pygame.K_c:
                    start = None
                    goal = None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()


main()