from collections import defaultdict
from collections import deque
def solution(n, results):
    answer = 0
    
    sort = defaultdict(list)
    reverse_sort = defaultdict(list)
    
    for winner, loser in results:
        sort[winner].append(loser)
        reverse_sort[loser].append(winner)
    
    for num in range(1, n+1):

        sortq = deque([num])
        rsortq = deque([num])
        
        s_set = set()
        
        while sortq:
            now = sortq.popleft()
            for next in sort[now]:
                if next not in s_set:
                    sortq.append(next)
                    s_set.add(next)
                    cnt += 1
        while rsortq:
            now = rsortq.popleft()
            for next in reverse_sort[now]:
                if next not in s_set:
                    rsortq.append(next)
                    s_set.add(next)
                    cnt += 1
                
        if cnt == n-1:
            answer += 1
            
    return answer
