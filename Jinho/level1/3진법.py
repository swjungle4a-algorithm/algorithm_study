def solution(n):
    third = []
    answer = 0
    while n:
        b = n%3
        third = [b] + third
        n = n//3
    for i in range(len(third)):
        answer += third[i] * 3 ** i
    return answer
