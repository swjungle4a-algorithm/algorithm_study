d = {0 : [-1, 0], 1 : [0, 1], 2 : [1, 0], 3 : [0, -1]}

def route_change(key, key_change):
    if key_change == "R":
        key = (key+1) % 4    
        
    elif key_change == "L":
        key = (key-1) % 4
    
    return key

def dfs(x, y, k, visited, grid):
    length = 0
    stack = [[x, y, k]]
    
    while stack:
        x, y, k = stack.pop()
        visited[x][y] = k
        
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and visited[nx][ny] == -1:
                k = route_change(k, grid[nx][ny])
                stack.append([nx, ny, k])
                length += 1
                
    return length, visited

def solution(grid):
    # len(grid[0]) : 가로, len(grid) : 세로
    w = len(grid[0])
    h = len(grid)
    answer = []
    
    for i in range(h):
        a = 0
        visited = [[-1] * len(grid[0]) for _ in range(len(grid))]
        for j in range(w):
            for k in range(4):
                length, tmp = dfs(i, j, k, visited, grid)
                a = length
                if not tmp:
                    break
            answer.append(a)
    return answer
