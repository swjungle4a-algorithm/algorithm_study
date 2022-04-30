def solution(n):
    answer = 0
    if n < 3 :
        return n
    
    tri = ""

    temp = n
    while temp :
        a, r = divmod(temp, 3)
        tri += r

    
    answer=int(tri,3)
    return answer
