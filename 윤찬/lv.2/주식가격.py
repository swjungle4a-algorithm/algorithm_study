from collections import deque
def solution(prices):
    size = len(prices) 
    answer = []
    que = deque(prices)
    idx = 0
    while que:
        cnt = 0
        price = que.popleft()
        for i in range(idx+1, size):
            cnt += 1
            if prices[i] < price: break
        answer.append(cnt)
        idx += 1
    return answer
