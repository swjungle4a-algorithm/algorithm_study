def solution(n, arr1, arr2):
    answer = []
    
    ans = [[]*n for _ in range(n)]
    
    for idx, i in enumerate(arr1):
        a = bin(i)[2:]
        while len(a) != n:
            a = '0'+str(a)
        tmp = ''
        for j in a:
            if j == '1':
                tmp += '#'
            else:
                tmp +=' '
        ans[idx].append(tmp)
        
    for idx, i in enumerate(arr2):
        a = bin(i)[2:]
        while len(a) != n:
            a = '0'+str(a)
        tmp = ''
        cnt = 0
        for j in a:
            if j == '1' or ans[idx][0][cnt]=='#':
                tmp += '#'
            elif j == '0' and ans[idx][0][cnt]==' ':
                tmp += ' '
            cnt+=1
        ans[idx] = tmp
    answer=ans    

    return answer
