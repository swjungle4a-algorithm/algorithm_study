from collections import deque

def bfs(x, y, n, wire):
    visited = [0] * (n)
    q = deque([x])
    visited[x], visited[y] = True, -1
    
    while q:
        x = q.popleft()
        for next_wire in wire[x]:
            if not visited[next_wire]:
                visited[next_wire] = True
                q.append(next_wire)
    
    return visited.count(True)

def solution(n, wires):
    answer = set()
    wire = [[] * n for _ in range(n)]
    
    for a, b in wires:
        a, b = a-1, b-1
        wire[a].append(b)
        wire[b].append(a)
    
    for current_wire in range(n):
        for connected_wire in wire[current_wire]:
            tmp = abs(bfs(current_wire, connected_wire, n, wire) - bfs(connected_wire, current_wire, n, wire))
            answer.add(tmp)

    return min(answer)
