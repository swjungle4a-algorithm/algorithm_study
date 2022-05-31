from collections import deque

def solution(n, results):
    answer = 0
    win_graph = [set() for _ in range(n+1)]
    lose_graph = [set() for _ in range(n+1)]

    for r in results :
        w, l = r
        win_graph[w].add(l)
        lose_graph[l].add(w)
    
    que = deque(results)
    while que :
        w, l = que.popleft()
        for loser in win_graph[l] :
            if loser in win_graph[w] :
                continue
            win_graph[w].add(loser)
            lose_graph[loser].add(w)
            que.append([w,loser])
            
    for i in range(1, n+1) :
        if len(win_graph[i] | lose_graph[i]) == n-1 :
            answer += 1

    return answer
