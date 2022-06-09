from collections import defaultdict
from heapq import heappush, heappop
def solution(n, t, m, timetable):
  
    answer = 540
    buses = defaultdict(list)
    for i in range(n):
        bus_t = 9*60 + t*i
        buses[bus_t] = []
        
    for time in timetable:
        hh, mm = map(int, time.split(':'))
        t = hh*60+mm
        for key in list(buses.keys()):
            if t<=key:
                heappush(buses[key], t)
                break
    yet = []
    for key in list(buses.keys()):
        n -= 1
        gone = []
        while len(yet)>0:
            heappush(buses[key], yet.pop())

        while buses[key] and len(gone)<m:       # 탄 애들
            gone.append(heappop(buses[key]))
        while buses[key]:                       # 못 탄 애들
            yet.append(heappop(buses[key]))
            
        if n==0:    # 막차
            if len(gone)<m:
                answer = key
            else:
                gone.sort()
                answer = gone[-1]-1
        
    h, m = map(str, divmod(answer, 60))
    answer = str(h.zfill(2))+':'+str(m.zfill(2))
    return answer
