def solution(prices):
    N = len(prices)
    answer = [0] * N
    stack = []
    
    for i in range(N-1):
        while stack and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    
    for i, s in stack:
        answer[i] = N - 1 - i
    
    return answer
