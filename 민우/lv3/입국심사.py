def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        
        for t in times:
            tmp += mid // t
            if tmp >= n:
                right = mid - 1
                break
            
        else:
            left = mid + 1
            answer = left
    
    return answer
