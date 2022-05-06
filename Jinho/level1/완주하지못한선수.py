def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    completion.append('NULL')

    for i, s in enumerate(participant):
        if s != completion[i]:
            return s
    
