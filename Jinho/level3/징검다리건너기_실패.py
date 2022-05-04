def solve(stones, left, right, k):
    
    length = len(stones)
    
    while left < right:
        
        mid = (left+right)/2
        
        cnt = 0
        
        while True:
            
            i = -1
            
            while i < length:
                
                if stones[i+1]:
                    i += 1
                    stones[i] -= 1
                    
                else:
                    flag = False
                    for jump in range(2, k+1):
                        if stones[i+jump]:
                            i += jump
                            stones[i] -= 1
                            flag = True
                            break
                            
                    if flag == False:
                        return False
                            
            cnt += 1
        
        if cnt < mid:
            right = mid + 1
        else:
            left = mid
                        
    return mid
    
    


def solution(stones, k):
    # 징검
    
    right = 200000000
    left = 0
    
        
    answer = solve(stones, left, right, k)
        

    return answer
