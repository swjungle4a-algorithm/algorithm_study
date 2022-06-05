def solution(n,a,b):
    answer = 0
    a = max(a, b)
    b = min(a, b)
    print(a, b)
    while abs(a-b) != 0:
        if a % 2 == 1:
            a = a // 2 - 1
        else:
            a //= 2
        
        if b % 2 == 1:
            b = b // 2 - 1
        else:
            b //= 2
        answer += 1
        print(a, b)
    
    return answer
