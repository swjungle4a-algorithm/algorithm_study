from heapq import heappush, heappop, heapify

def solution(n, works):
    heapify(works := list(map(lambda x: -x,works)))
    while n :
        if (work := -heappop(works)) == 0 : break
        heappush(works, -work + 1)
        n -= 1
    return sum(map(lambda x : x ** 2, works))
