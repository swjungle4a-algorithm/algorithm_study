from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que = deque()
    que.append(cities[0].lower())
    chk = {cities[0].lower() : 1}
    runtime = 5
    
    for city in cities[1:] :
        city = city.lower()
        if city in que :
            runtime += 1
            chk[city] += 1
            continue
        
        runtime += 5
        if len(que) == cacheSize :
            if min(chk.values()) == max(chk.values()) :
                select = que.popleft()
                chk.pop(select)
            else :
                select = min(chk)
                chk.pop(select)
                que.remove(select)
        que.append(city)
        chk[city] = 1
    answer = runtime
    return answer
