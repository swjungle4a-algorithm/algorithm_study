def solution(n, t, m, timetable):
    answer = 0
    wait_time, bus_time = [], []
    
    # 크루가 줄을 선 시간
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        wait_time.append((hour*60) + minute)
    wait_time.sort()
    
    # 버스 도착 시간
    for i in range(n):
        bus_time.append(540 + (i * t))
    
    # Logic (완전탐색 넉낌 낭낭)
    i = 0
    
    for time in bus_time:
        cnt = 0
        while i < len(wait_time) and wait_time[i] <= time and cnt < m:
            i += 1
            cnt += 1

        answer = time if cnt < m else wait_time[i - 1] - 1 # else means "cnt == m"
        
    return str(answer//60).zfill(2) + ":" + str(answer%60).zfill(2)
