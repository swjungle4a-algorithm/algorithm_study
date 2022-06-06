from bisect import bisect_left

def check(arr, n) :
    p = bisect_left(arr, n)
    if n <= len(arr[p:]) :
        return True
    return False
    
def solution(citations):
    answer = 0
    citations.sort()
    for c in range(len(citations),0,-1) :
        if check(citations, c) :
            return c
    else :
        return 0
