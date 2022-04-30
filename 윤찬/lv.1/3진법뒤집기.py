def solution(n):
    answer = 0
    three = 1
    temp = []

    while n > 0:
        temp.append(n % 3)
        n //= 3

    for i in range(len(temp)-1, -1, -1):
        answer += temp[i] * three
        three *= 3

    return answer
