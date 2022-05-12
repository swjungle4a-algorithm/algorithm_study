from collections import defaultdict

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    dic = defaultdict(set)
    
    for r in report:
        user, reported_user = r.split()
        dic[reported_user].add(user)
    
    for report_list in dic.values():
        if len(report_list) >= k:
            for id in report_list:
                answer[id_list.index(id)] += 1
    
    return answer
