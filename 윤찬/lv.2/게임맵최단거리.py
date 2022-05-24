from collections import deque
def solution(maps):
    answer = 0
    direction = ((1,0), (-1,0), (0,1), (0,-1)) 
    queue = deque([[0,0]])
    row = len(maps)
    col = len(maps[0])

    while queue:
        x, y = queue.popleft()
        if x == row-1 and y == col-1: return maps[row - 1][col - 1]
        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            if 0 > new_x or row <= new_x or 0 > new_y or col <= new_y: continue
            if maps[new_x][new_y] == 1:
                maps[new_x][new_y] = maps[x][y] + 1
                queue.append((new_x, new_y))
    return -1
