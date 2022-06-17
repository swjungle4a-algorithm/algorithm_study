def solution(money):
    if len(money) <= 3:
        return max(money)
    N = len(money)
    answer = []
    
    dp = [0] * N
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    
    for i in range(2, N-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    answer.append(dp[-2])

    dp = [0] * N
    dp[0] = 0
    dp[1] = money[1]
    
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    answer.append(dp[-1])

    return max(answer)
