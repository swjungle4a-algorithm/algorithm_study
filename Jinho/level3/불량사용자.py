from itertools import product
def solution(user_id, banned_id):

    id_list = [[] for _ in range(len(banned_id))]
    
    for idx, banid in enumerate(banned_id):
        for userid in user_id:
            length = len(userid)
            
            if len(banid) != len(userid):
                continue
            
            for i in range(length):
                if banid[i] == '*':
                    pass
                elif banid[i] != userid[i]:
                    break
            else:
                id_list[idx].append(userid)

    answer = set()
    
    sizeofban = len(banned_id)
    for i in product(*id_list):
        if len(set(i)) == sizeofban:
            answer.add(tuple(sorted(i)))
    
    return len(answer)
