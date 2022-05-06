def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    # for person in participant:
        # if participant.count(person) != completion.count(person):
        #     answer = person
    idx = 0
    for p, c in zip(participant, completion):
        if p!=c: 
            answer = p
            break
        idx += 1
    else:
        answer = participant[idx]
        
    return answer
