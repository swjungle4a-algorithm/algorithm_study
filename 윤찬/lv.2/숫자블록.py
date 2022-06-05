def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        if i == 1: 
            answer.append(0)
            continue
        tmp = int(i**0.5)
        for j in range(2, tmp+1):
            val = i // j
            if val > 10**7: continue
            if i % j == 0:
                answer.append(i//j)
                break
        else:
            answer.append(1)    
    return answer
