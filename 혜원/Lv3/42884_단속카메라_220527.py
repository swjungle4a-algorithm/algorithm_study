def solution(routes):
    answer = 1 # 0
    routes.sort(key = lambda x:x[1])
    point = routes[0][1] # -30001
    print(routes)
    for route in routes:
        if route[0] <= point: #  <= route[1]:
            continue
        else:
            point = route[1]
            answer+=1
    return answer
