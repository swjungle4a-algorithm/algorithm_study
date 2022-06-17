def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2 :
        return max(sticker)

    dp = sticker[0:]
    dp[-1] = 0

    dp[1] = sticker[0]
    
    dp2 = sticker[0:]
    dp2[0] = 0

    for idx, val in enumerate(dp[2:], start=2):
        dp[idx] = max(dp[idx-2]+val, dp[idx-1])
        
    for idx, val in enumerate(dp2[2:], start=2):
        dp2[idx] = max(dp2[idx-2]+val, dp2[idx-1])

    return max(dp[len(dp)-1],dp2[len(dp2)-1])  
