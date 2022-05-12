```python3
from collections import deque

def change(graph, x, y, direction):
    len_x = len(graph)
    len_y = len(graph[0])
    
    if graph[x][y] == 'S':
        if direction == 'N':
            x = (x - 1) % len_x
        elif direction == 'E':
            y = (y + 1) % len_y
        elif direction == 'S':
            x = (x + 1) % len_x
        elif direction == 'W':
            y = (y - 1) % len_y
    elif graph[x][y] == 'R':
        if direction == 'N':
            y = (y + 1) % len_y
        elif direction == 'E':
            x = (x - 1) % len_x
        elif direction == 'S':
            y = (y - 1) % len_y
        elif direction == 'W':
            x = (x + 1) % len_x
    elif graph[x][y] == 'L':
        if direction == 'N':
            y = (y - 1) % len_y
        elif direction == 'E':
            x = (x + 1) % len_x
        elif direction == 'S':
            y = (y + 1) % len_y
        elif direction == 'W':
            x = (x - 1) % len_x
            
    x = len_x if x == -1 else x
    y = len_y if y == -1 else y
    
    return (x, y)

def solution(grid):
    answer = []
    graph = []
    
    for row in grid:
        graph.append(list(row))
    
    # print(graph)
    
    direction = ['N','E','S','W']
    
    len_x = len(graph)
    len_y = len(graph[0])
    
    entries = set()
    
    for x in range(len_x):
        entries.add((x, 0, 'W'))
        entries.add((x, 0, 'E'))
        if len_x > 1:
            entries.add((x, len_y - 1, 'W'))
            entries.add((x, len_y - 1, 'E'))
        
    for y in range(len_y):
        entries.add((0, y, 'S'))
        entries.add((0, y, 'N'))
        if len_y > 1:
            entries.add((len_x - 1, y, 'S'))
            entries.add((len_x - 1, y, 'N'))
    
    for entry in entries:
        q = deque([entry])
        count = 1
        
        while 1:
            now_x, now_y, direction = q.popleft()
            # 작성중 (실패)
        
    
    
    return answer
```
