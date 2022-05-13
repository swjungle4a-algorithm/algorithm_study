
def solution(id_list, report, k):
    answer = []
    reports = list(set(report))
    black_list = dict()
    msg = dict()
    for id in id_list:
        black_list[id] = []
        msg[id] = 0
    
    for singo in reports:
        reporter, reported = singo.split()
        black_list[reported].append(reporter)
        
    for user in id_list:
        if len(black_list[user])>=k:
            for i in black_list[user]:
                msg[i]+=1
                
    answer = list(msg.values())
    return answer
