from collections import deque

def solution(cacheSize, cities):    
    answer = 0
    cache = deque(maxlen = cacheSize)

    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            del cache[cache.index(city)]
            
        else:
            answer += 5
            
        cache.append(city)
    
    return answer
