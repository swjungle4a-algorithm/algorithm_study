from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    
    dicts = defaultdict(list)
    dict_id = defaultdict(list)
    
    for name in id_list:
        dicts[name].append(0) 
    
    for rep in report:
        a, b = rep.split(' ')
        dict_id[b].append(a)

    for name in id_list:
        if len(set(dict_id[name])) >= k:
            for mail in set(dict_id[name]):
                dicts[mail][0] += 1

    for name in dicts.keys():
        answer.extend(dicts[name])
    
    return answer
