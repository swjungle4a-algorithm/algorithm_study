def solution(prices):
    answer = [0]*len(prices)
    
    stk = []
    stk.append([prices[0], 0])
    answer[0] = 0
    
    for idx, price in enumerate(prices[1:], start=1):
        for i in stk:
            answer[i[1]] += 1
        if stk and stk[-1][0] > price:
            while stk and stk[-1][0] > price:
                stk.pop()
        stk.append([price, idx])
    
    return answer
