def solution(citations):
    answer = 0
    h = 0
    k = 0
    citations.sort()
    tmp = len(citations)
    
    for i in range(tmp):
        h = citations[i]
        k = tmp - i
        if k <= h:
            return k
    return k
