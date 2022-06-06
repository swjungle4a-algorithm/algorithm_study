def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stk = []
    stk.append((0,prices[0]))
    for idx, price in enumerate(prices[1:], 1) :
        while stk and stk[-1][1] > price :
            i, p = stk.pop()
            answer[i] = idx - i
        stk.append((idx, price))
    
    while stk :
        i, p = stk.pop()
        answer[i] = len(prices) - i - 1
    return answer
