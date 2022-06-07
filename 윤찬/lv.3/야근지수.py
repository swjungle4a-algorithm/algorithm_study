from heapq import heappush, heappop, heapify
def solution(n, works):
    heapify(works := list(map(lambda x: -x, works)))
    for _ in range(n): 
        heappush(works, heappop(works) + 1)
    return sum(map(lambda x: 0 if -x < 0 else (-x)**2, works))
