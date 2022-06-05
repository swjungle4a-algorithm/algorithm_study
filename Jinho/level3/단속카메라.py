def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    end = -30001
    for now_start, now_end in routes:
        if now_start <= end <= now_end:
            continue
        else:
            answer += 1
            end = now_end
    return answer
