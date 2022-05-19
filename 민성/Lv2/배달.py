from collections import defaultdict, deque
def solution(N, road, K):
    INF = 10**9
    distances = [INF] * (N+1)
    
    adj_list = [[]*(N+1) for _ in range(N+1)]
    
    for a,b,c in road:
        adj_list[a].append((c,b))
        adj_list[b].append((c,a))
    
    dq = deque()
    dq.append((0,1))
    distances[1] = 0
    while dq:
        cost, dest = dq.pop()
        for ct, nd in adj_list[dest]:
            if distances[nd] > cost + ct:
                distances[nd] = cost + ct
                dq.append((distances[nd], nd))  

    return sum(1 for i in distances[1:] if i<=K)
