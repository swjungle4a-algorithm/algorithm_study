from itertools import combinations

def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.append(distance)
    rocks.sort()
    while left<right:
        mid = (left+right)//2
        start, cnt = 0, 0
        for end in rocks:
            if end - start <= mid:
                cnt += 1
            else:
                start = end
        if cnt > n:
            right = mid
        else:
            left = mid+1
        
    return left
