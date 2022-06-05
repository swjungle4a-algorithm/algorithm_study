def solution(number, k):
    answer = []
    N = k
    
    for num in number:
        while k and answer and num > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(num)
    
    while len(answer) >= len(number):
        answer.pop()
    
    return "".join(answer)
