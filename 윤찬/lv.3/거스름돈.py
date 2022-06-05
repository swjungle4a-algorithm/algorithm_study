def solution(n, money):
    dp = [1] + [0] * n
    
    for i in range(1, n+1):
        for coin in money:
            div, mod = divmod(i, coin)
            if mod == 0: dp[i] += 1
            else:
                if i >= coin:
                    dp[i] += dp[i-coin]
    return dp[n] % 1000000007
