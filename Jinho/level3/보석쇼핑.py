from collections import deque, defaultdict

def solution(gems):
    
    de_list = defaultdict(int)
    
    maxlen = len(gems)
    min_value = 1000000000
    target = len(set(gems))
    end = 0
    
    for i, gem in enumerate(gems):
        
        while len(de_list) < target and end < maxlen:
            
            de_list[gems[end]] += 1
            end += 1
            
        if len(de_list) == target and end-i < min_value:
            min_value = end-i
            answer = [i+1, end]
        
        de_list[gem] -= 1
        if de_list[gem] == 0:
            del de_list[gem]
    
    return answer
