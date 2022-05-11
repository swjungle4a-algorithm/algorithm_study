from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que = deque(maxlen = cacheSize)
    
    for city in cities :
        city = city.lower()
        if city in que :
            answer += 1
            que.remove(city)
            que.append(city)
            continue
        
        answer += 5
        que.append(city)
        
    
    
    return answer
