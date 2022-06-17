def solution(sticker):
    N = len(sticker)
    if N <= 2:
        return max(sticker)

    answer = []

    # case 1 - 첫 번째 스티커를 떼지 않는 경우
    dp = [0] * N
    dp[0] = 0
    dp[1] = sticker[1]
    dp[2] = max(sticker[1], sticker[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])

    answer.append(dp[-1])

    # case 2 - 첫 번째 스티커를 떼는 경우
    dp = [0] * N
    dp[0] = sticker[0]
    dp[1] = sticker[1]
    dp[2] = max(sticker[0] + sticker[2], sticker[1])

    for i in range(3, N - 1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1], dp[i-3] + sticker[i])

    answer.append(dp[-2])

    return max(answer)
