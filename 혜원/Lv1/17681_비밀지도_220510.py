def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        n1, n2 = int(num1), int(num2)
        tmp = bin(n1|n2)
        ans = ''
        for t in range(len(tmp)-1, -1, -1):
            if not tmp[t].isdigit():
                break
            ans = '#'+ans if tmp[t]=='1' else ' '+ans
        else:
            continue
        while len(ans)<n:
            ans = ' '+ans
        answer.append(ans)
    return answer
