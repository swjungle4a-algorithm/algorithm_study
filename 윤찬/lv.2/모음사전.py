d = {0: 'A', 1: 'E', 2: 'I', 3: 'O', 4: 'U'}

def dfs(tmp, depth, arr):
    if depth == 5: return

    for i in range(5):   
        tmp += d[i]
        arr.append(tmp)
        dfs(tmp, depth+1, arr)
        tmp = tmp[:-1]
    return arr

def solution(word):
    return dfs('', 0, []).index(word)+1
