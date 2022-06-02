def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    tmp = routes[0][0] - 1

    for r_start, r_end in routes:
        if r_start > tmp:
            answer += 1
            tmp = r_end
    
    return answer
