def bisect(target, stones,k):
    cnt = 0
    
    for stone in stones:
        if stone-target <= 0:
            cnt += 1
        else:
            cnt = 0   
            
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    answer = 0

    l = 0
    r = max(stones)
    
    while(True):
        if l > r:
            break
    
        mid = (l + r) // 2
        
        flag = bisect(mid, stones, k)
        if not flag:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
       
    return answer
