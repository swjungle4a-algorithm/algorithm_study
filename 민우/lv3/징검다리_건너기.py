# 최소값 중 최대값 구하기?

def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        
        for stone in stones:
            if stone - mid <= 0:
                tmp += 1
                if tmp == k:
                    right = mid - 1
                    break

            else:
                tmp = 0
                
        else:
            left = mid + 1
            answer = left
    
    return answer
