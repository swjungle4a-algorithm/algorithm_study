def solution(s, n):
    lower_alpha = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = lower_alpha.upper()
    answer = ""
    
    for i in s:
        if i in lower_alpha:
            answer += lower_alpha[(lower_alpha.index(i) + n) % 26]
        elif i in upper_alpha:
            answer += upper_alpha[(upper_alpha.index(i) + n) % 26]
        else:
            answer += " "
            
    return answer
