def solution(n, times):
    answer, left, right = 0, 1, min(times)*n
    while left <= right :
        mid = (left + right) // 2
        if sum(map(lambda t: mid // t, times)) >= n :
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    return answer
