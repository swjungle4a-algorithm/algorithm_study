from collections import Counter

def solution(id_list, report, k):
    answer = {x : 0 for x in id_list}
    report = set(report)
    c = Counter(map(lambda x : x.split()[1], report))
    
    for rp in report :
        reporter, reportee = rp.split()
        if c[reportee] >= k :
            answer[reporter] += 1
    answer = list(answer.values())
    return answer
