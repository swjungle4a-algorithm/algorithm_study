from collections import defaultdict

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    dic = defaultdict(set)
    
    for r in report:
        user, reported_user = r.split()
        dic[reported_user].add(user)
    
    for i in dic.keys():
        if len(dic[i]) >= k:
            for j in dic[i]:
                answer[id_list.index(j)] += 1
    
    return answer
