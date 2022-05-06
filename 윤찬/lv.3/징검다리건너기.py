def solution(stones, k):
    result = 0
    start = 0
    end = max(stones[:k])
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if k == cnt:
                end = mid - 1
                break
        else:
            start = mid + 1
            result = start

    return result
