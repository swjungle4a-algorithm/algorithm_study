import heapq
def solution(cacheSize, cities):
    if cacheSize == 0: return len(cities) * 5

    answer = cacheSize * 5
    tmp = []
    for i in range(cacheSize):
        heapq.heappush(tmp, [i, cities[i]])
    size = cacheSize - 1
    for i in cities[cacheSize:]:
        size += 1
        for j in tmp:
            if i.lower() == j[1].lower():
                answer += 1
                tmp.remove(j)
                break
        else:
            answer += 5
            heapq.heappop(tmp)
        heapq.heappush(tmp, [size, i])
        
            
    return answer
