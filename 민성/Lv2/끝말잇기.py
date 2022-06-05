from math import ceil
def solution(n, words):
    answer = []
    tmp = []
    
    ans = 0
    for idx, word in enumerate(words, start=1):
        if not tmp:
            tmp.append(word)
            continue

        if tmp[-1][-1] == word[0] and not word in tmp:
            tmp.append(word)
            continue
        else:
            ans = idx
            break        
        
    if ans == 0:
        return [0,0]
    else:
        idx = idx % n 
        if not idx:
            idx += n
        answer.append(idx)
        answer.append(ceil(ans/n))

    return answer
