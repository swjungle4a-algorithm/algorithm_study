def solution(arr):
    answer = [0, 0]
    N = len(arr)
    
    def dnc(x, y, N):
        start = arr[x][y]

        for i in range(x, x+N):
            for j in range(y, y+N):
                if start != arr[i][j]:
                    N //= 2
                    dnc(x, y, N)
                    dnc(x+N, y, N)
                    dnc(x, y+N, N)
                    dnc(x+N, y+N, N)
                    return

        answer[start] += 1
    
    dnc(0, 0, N)
    
    return answer
