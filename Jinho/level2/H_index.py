def solution(citations):
    citations.sort(reverse=True)
    length = len(citations)
    for i, c in enumerate(citations):
        if c <= i+1:
            return max(c, i)
    else:
        return length
