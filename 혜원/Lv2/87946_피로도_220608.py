from itertools import permutations

def solution(k, dungeons):
    answer = -1
    cases = list(permutations(dungeons))
    n = len(dungeons)
    
    for case in cases:
        base = k
        cnt = 0
        for i in range(n):
            if base<case[i][0]: break
            else:
                base -= case[i][1]
                cnt += 1
        answer = max(answer, cnt)
            
    return answer
