# 실패

def solution(grid):
    answer = []
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dirxs = {"L" : -1, "R" : 1, "S" : 0}
    for origin_dirx in range(4) :
        dirx = origin_dirx
        max_r = len(grid)
        max_c = len(grid[0])
        start = grid[0][0]
        r = (0 + dr[dirx]) % max_r
        c = (0 + dc[dirx]) % max_c
        len_cycle = 1
        dirx = (dirx + dirxs[grid[r][c]]) % 4
        nr = (r + dr[dirx]) % max_r
        nc = (c + dc[dirx]) % max_c
        
        while dirx != origin_dirx or (nr != r or nc != c) :
            dirx = (dirx + dirxs[grid[nr][nc]]) % 4
            len_cycle += 1
            nr = (nr + dr[dirx]) % max_r
            nc = (nc + dc[dirx]) % max_c
        answer.append(len_cycle)
    return answer
