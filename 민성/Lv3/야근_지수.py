import heapq

def solution(n, works):
    
    for idx, work in enumerate(works):
        works[idx] = -work
    
    heapq.heapify(works)
    
    for idx in range(n):
        heapq.heappush(works, heapq.heappop(works)+1)
    
    return sum([work**2 for work in works if work < 0])
