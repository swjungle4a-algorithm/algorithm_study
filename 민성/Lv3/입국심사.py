def solution(n, times):
    answer = 0 
    p = 0
    q = max(times) * n
    
    while True:
        if p > q:
            break
        
        mid = (p+q)//2
        tmp = 0

        for time in times:
            tmp += (mid//time)
    
        if tmp < n:
            answer= mid
            p = mid + 1
        else:
            q = mid - 1

    return answer+1
