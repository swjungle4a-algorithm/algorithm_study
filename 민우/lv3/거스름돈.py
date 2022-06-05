# dp[현재해당가격] += dp[현재해당가격 - 현재화폐의액수]

def solution(n, money):
    dp = [1] + [0] * n
    for m in money:
        for i in range(m, n+1):
            if i >= m:
                dp[i] += dp[i-m]
    return dp[n] % 1000000007
