def solution(stones, k):
    answer = 0

    left = 0
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
                if cnt == k:
                    right = mid - 1
                    break
            else:
                cnt = 0
        else:
            left = mid + 1
            answer = left

    return answer
