def solution(n, money):
    answer = 0
    
    dp = [1] + [0]*n
    
    for coin in money:
        for price in range(coin, n+1):
            if price >= coin:
                dp[price] += dp[price-coin]
    
    return dp[n] % 10000000007
