from collections import deque
def solution(grid):
    answer = []
    arr = []
    visited = []
    direction = ((-1,0), (1,0), (0,-1), (0,1))
    for str in grid:
        temp = []
        for c in str:
            temp.append(c)
            visited.append([0,0,0,0])
        arr.append(temp)
        
    print(visited)
    queue = deque([[0,0]])
    # while queue:
    #     x, y = queue.pop()
    #     for dx, dy in direction:
    #         new_x = x + dx
    #         new_y = y + dy
            
    return answer
