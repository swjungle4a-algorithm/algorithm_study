def solution(n, times):
    answer = 0
    
    start, end = 1, times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        total = 0
        
        for time in times:
            total += mid //time

        if total < n:
            start = mid + 1
        else:
            end = mid - 1
            
    answer = start
    return answer
