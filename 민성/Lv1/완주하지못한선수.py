from collections import Counter
def solution(participant, completion):
    answer = tuple(set(participant)-set(completion))
    if answer:
        return answer[0]
    
    start = Counter(participant).most_common()
    end = Counter(completion).most_common()

    for i in start:
        for j in end:
            if i[0] == j[0]:
                if i[1] != j[1]:
                    return i[0]
    
    return answer
