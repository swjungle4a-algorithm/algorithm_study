def solution(sizes):
    left = max(map(max, sizes))
    right = max(map(min, sizes))
    answer = left * right
    return answer 
