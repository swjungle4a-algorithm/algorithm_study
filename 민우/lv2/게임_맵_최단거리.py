from collections import deque

def solution(maps):
    def bfs():
        w, h = len(maps), len(maps[0])
        q = deque([[0, 0]])
        # visited = [[False] * h for _ in range(w)]
        # visited[0][0] = True

        while q:
            x, y= q.popleft()

            if x == w - 1 and y == h - 1:
                return maps[x][y]

            for i in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = x + i[0]
                ny = y + i[1]

                if 0 <= nx < w and 0 <= ny < h and maps[nx][ny] == 1:
                    # visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    q.append([nx, ny])

        return -1

    return bfs()
