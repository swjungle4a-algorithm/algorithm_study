def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for i, citation in enumerate(citations):
        if n-i <= citation:
            answer = n-i
            break
        
    return answer
