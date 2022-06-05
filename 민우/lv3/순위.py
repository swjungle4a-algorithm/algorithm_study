from collections import deque

def bfs(x, lists, n):
    visited = [False] * n
    visited[x] = True
    q = deque([x])
    
    while q:
        x = q.popleft()
        
        for i in lists[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
    return visited.count(True)

def solution(n, results):
    answer = 0
    winner_list = [[] for _ in range(n)]
    loser_list = [[] for _ in range(n)]
    
    for winner, loser in results:
        winner, loser = winner - 1, loser - 1
        winner_list[winner].append(loser)
        loser_list[loser].append(winner)
    
    
    for i in range(n):
        tmp = bfs(i, winner_list, n) + bfs(i, loser_list, n)
        if tmp == n+1:
            answer += 1
    
    return answer
