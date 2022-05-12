from collections import Counter

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    c = Counter(map(lambda x : x.split()[1], report))
    
    for rp in report :
        reporter, reportee = rp.split()
        if c[reportee] >= k :
            answer[id_list.index(reporter)] += 1
    return answer
