def solution(citations):
    answer = 0
    citations.sort()
    
    for idx in range(len(citations)):
        if citations[idx] >= len(citations[idx:]):
            answer = max(answer, len(citations[idx:]))
    
    return answer
