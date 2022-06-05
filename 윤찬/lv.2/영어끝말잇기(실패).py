def solution(n, words):
    answer = []
    tmp = []
    size = len(words)
    div, mod = divmod(size, n)
    
    for i in range(n):
        start = i
        tmp1 = []
        while start < size:
            tmp1.append(words[start])
            start += n
        tmp.append(tmp1)
    print(tmp)
    b = div if mod == 0 else div + 1
    s = tmp[0][0][-1]
    print(s)
    # for i in range(b):
    #     for j in range(n):
    #         s = tmp[j][i][0]
    
    return answer
