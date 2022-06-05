def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    end = routes[0][1]
    answer = 1
    for route_start, route_end in routes[1:]:
        if end >= route_start: continue
        end = route_end
        answer += 1
        
    return answer
