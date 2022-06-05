def solution(arr):
    answer = [0, 0]
    def zip_arr(a, b, size):
        status = arr[a][b]
        for i in range(a, a + size):
            for j in range(b, b + size):
                if arr[i][j] != status:
                    size = size//2
                    zip_arr(a, b, size)
                    zip_arr(a + size, b, size)
                    zip_arr(a, b + size, size)
                    zip_arr(a + size, b + size, size)
                    return
        answer[status] += 1
    zip_arr(0, 0, len(arr))
    return answer
