from queue import deque
from copy import deepcopy
def turn(key):  
    new_key = deque()
    for cols in zip(*key):
        new_key.appendleft(cols)
    return new_key

def solution(key, lock):
    answer = True
    holes, stones = [], []
    n, m = len(lock), len(key)
    
    for i in range(n):
         for j in range(n):
            if lock[i][j] == 0:
                holes.append((i, j))
            else:
                stones.append((i, j))
    if len(holes) == 0:
        return True
    for case in range(4):
        keys = []
        for i in range(m):
            for j in range(m):
                if key[i][j] == 1:
                    keys.append((i-(m-1),j-(m-1)))
        for size_r in range(n+m-1):
            for size_c in range(n+m-1):
                unlocked = set()
                for row, col in keys:
                    if (row+size_r, col+size_c) in stones:
                        break
                    if (row+size_r, col+size_c) in holes:
                        unlocked.add((row+size_r, col+size_c))
                    if len(unlocked) == len(holes):
                        return True
                    
        key = turn(key)

    return False
