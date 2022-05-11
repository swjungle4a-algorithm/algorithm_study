from collections import deque
def solution(cacheSize, cities):
    dq = deque()
    answer = 0
    if not cacheSize:
        return 5*len(cities)
        
    for city in cities:
        city = city.lower()
        if city in dq:
            answer += 1
            dq.remove(city)
            dq.appendleft(city)
        else:
            answer += 5
            if len(dq) == cacheSize:
                dq.pop()
            dq.appendleft(city)
                             
    return answer
