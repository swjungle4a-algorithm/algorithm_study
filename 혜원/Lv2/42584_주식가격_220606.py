def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n): 
        cnt = 1
        for j in range(i+1, n):
            if prices[i]<=prices[j]: cnt += 1
            else: break
        else:
            cnt -= 1    
        answer.append(cnt)                
        
    return answer
