def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        cnt = 0
        for j in range(i+1, length):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer
