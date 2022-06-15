def solution(triangle): 
    N = len(triangle)
    
    dp = [[0]*i for i in range(1,N+1)]
    
    for i, tri in enumerate(triangle[N-1]):
        dp[len(triangle)-1][i] = tri
    
    for idx1, tri in enumerate(triangle[N-1:0:-1], start=1):
        idx1 = N-idx1
        len_tri = len(tri)-1
        for idx2 in range(len(tri)):  
            cur = dp[idx1][idx2]
            if idx2 == 0 :
                dp[idx1-1][idx2] = max(cur + triangle[idx1-1][idx2], dp[idx1-1][idx2])
            elif idx2 == idx1:
                dp[idx1-1][idx2-1] = max(cur + triangle[idx1-1][idx2-1], dp[idx1-1][idx2-1])
            else:
                dp[idx1-1][idx2] = max(cur + triangle[idx1-1][idx2], dp[idx1-1][idx2])
                dp[idx1-1][idx2-1] = max(cur + triangle[idx1-1][idx2-1], dp[idx1-1][idx2-1])                             

    return dp[0][0]
