from collections import defaultdict
def solution(id_list, report, k):
    report = set(report)
    report2 = defaultdict(list)
    answer = [0] * len(id_list)
    for name in report:
        name = name.split(' ')
        report2[name[1]].append(name[0])
    for key in report2:
        tmp = report2[key]
        if len(tmp) >= k:
            for s in tmp:
                answer[id_list.index(s)] += 1
    return answer
