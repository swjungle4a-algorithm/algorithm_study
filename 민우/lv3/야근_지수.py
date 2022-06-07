from heapq import heappush, heappop

def solution(n, works):
    heap = []
    
    for work in works:
        heappush(heap, (-work, work))
    
    for _ in range(n):
        x = heappop(heap)[1] - 1
        if x < 0:
            return 0
        heappush(heap, (-x, x))
    
    return sum(x**2 for _, x in heap)
