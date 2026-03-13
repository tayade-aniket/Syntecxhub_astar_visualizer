from queue import PriorityQueue

def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def astar(draw, grid, start, goal):

    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic(start.get_pos(), goal.get_pos())

    open_hash = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_hash.remove(current)

        if current == goal:
            reconstruct_path(came_from, goal, draw)
            goal.make_goal()
            return True

        neighbors = []

        r, c = current.get_pos()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for d in directions:
            nr = r + d[0]
            nc = c + d[1]

            if 0 <= nr < len(grid) and 0 <= nc < len(grid):
                neighbor = grid[nr][nc]
                if not neighbor.is_wall():
                    neighbors.append(neighbor)

        for neighbor in neighbors:

            temp_g = g_score[current] + 1

            if temp_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + heuristic(
                    neighbor.get_pos(), goal.get_pos())

                if neighbor not in open_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False