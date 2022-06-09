from collections import defaultdict

def solution(n, t, m, timetable):
    boarders = defaultdict()
    timetable.sort(reverse=True)
    time = "09:00"
    
    for time_index in range(n) :
        bus_hour, bus_minute = map(int,time.split(":"))
        bus_hour += (time_index * t) // 60
        bus_minute = (bus_minute + time_index * t) % 60
        now_bus_time = "%02d:%02d"%(bus_hour,bus_minute)
        boarders[now_bus_time] = []
        
        while timetable and timetable[-1] <= now_bus_time and len(boarders[now_bus_time]) < m :
            boarders[now_bus_time].append(timetable.pop())
    
    last_bus_time = max(boarders)
    if len(boarders[last_bus_time]) < m :
            answer = last_bus_time
    else :
        h, m = map(int,boarders[last_bus_time][-1].split(":"))
        if m > 0 :
            answer = "%02d:%02d"%(h,m-1)
        else :
            answer = "%02d:%02d"%(h-1,59)
    return answer
