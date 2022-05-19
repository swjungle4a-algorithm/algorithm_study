def solution(n, times):
        
    times.sort()
    left, right = 0, max(times)*n
    while left<=right:        
        mid = (left+right)//2       # 소요시간
        people = 0
        for time in times:
            people += mid//time
        if people>=n: 
            right = mid-1
            answer = mid
        else: 
            left = mid+1
        
    return answer
