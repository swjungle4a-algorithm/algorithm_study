def solution(distance, rocks, n):

    left = 0
    right = distance
    
    length = len(rocks)
    rock = [0] + rocks + [distance]
    rocks.sort()

    while left < right:
        mid = (left + right) // 2
        rocklist = [0]
        cnt = n
        for rock in rocks:
            rocklist.append(rock)
            if rocklist[-1] - rocklist[-2] < mid:
                rocklist.pop()
                cnt -= 1
        
        if cnt < 0:
            right = mid
        else:
            left = mid + 1
            
    return left - 1
