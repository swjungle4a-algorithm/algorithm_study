def solution(a):
    answer = 2
    
    min_value = 1000000001
    
    length = len(a)
    
    left = [0] * length
    right = [0] * length
    
    for i in range(length):
        
        min_value = min(min_value, a[i])
        
        left[i] = min_value
        
    min_value = 1000000001
    
    for i in range(length-1, -1, -1):
        
        min_value = min(min_value, a[i])
        
        right[i] = min_value
        
    for i in range(1, length-1):
        
        if a[i] > left[i] and a[i] > right[i]:
            continue
        else:
            answer += 1
        
    return answer
