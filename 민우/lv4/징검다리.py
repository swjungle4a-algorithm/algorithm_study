def solution(distance, rocks, n):
    left = 0
    right = distance
    rocks.sort()

    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        result = 0

        for rock in rocks:
            if rock - tmp < mid:
                result += 1
                
            else:
                tmp = rock

        if result <= n:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return right
