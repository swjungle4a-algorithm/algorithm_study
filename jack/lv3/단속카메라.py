def solution(routes):
    answer = 1
    routes.sort(key= lambda x: x[1])
    camera = routes[0][1]
    for route in routes[1:] :
        s, e = route
        if s <= camera and camera <= e :
            continue
        camera = e
        answer += 1
    return answer
