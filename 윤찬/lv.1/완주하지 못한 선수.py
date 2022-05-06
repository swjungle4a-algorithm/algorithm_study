from collections import Counter
def solution(participant, completion):
    answer = ''
    completion_arr = Counter(completion)

    for i in participant:
        if completion_arr[i] == 0:
            return i
        
        completion_arr[i] -=1