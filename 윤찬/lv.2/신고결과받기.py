from collections import Counter
def solution(id_list, report, k):
    answer = {}
    tmp = []
    d = {}
    for str in report:
        user, reported = str.split()
        if user not in d:
            d[user] = [reported]
            tmp.append(reported)
        else:
            if reported in d[user]: continue
            d[user] += [reported]
            tmp.append(reported)
    a = Counter(tmp)
    for i in d:
        cnt = 0
        for j in d[i]:
            if a[j] >= k:
                cnt += 1
        answer[i] = cnt
    result = [0] * len(id_list)
    idx = 0
    for i in id_list:
        if i in answer:
            result[idx] = int(answer[i])
        idx += 1
    return result
