def solution(stones, k):
    start = 0
    end = max(stones)
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for stone in stones:
            if stone - mid <= 0: cnt += 1
            else: cnt = 0 
            if k == cnt:
                end = mid - 1
                break
            
        if cnt < k:
            start = mid + 1
            result = mid

    return result