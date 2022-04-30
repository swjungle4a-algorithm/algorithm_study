def solution(n):
    answer = 0
    if n < 3 :
        return n
    
    tri = ""

    temp = n
    while temp :
        tri += str(temp%3)
        temp = temp // 3

    
    for i in range(len(tri)) :
        answer += int(tri[i]) * (3 ** (len(tri)-i-1))
        
    return answer
