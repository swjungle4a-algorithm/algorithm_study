from collections import Counter

def solution(participant, completion):
    answer = ''
    
    hashed_comp = Counter(completion)
    for p in participant :
        if hashed_comp[p] > 0:
            hashed_comp[p] -= 1
        else :
            answer = p
            break
    return answer
