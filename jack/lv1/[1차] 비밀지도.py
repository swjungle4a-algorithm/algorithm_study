def solution(n, arr1, arr2):
    answer = []
    arr = [i | j for i,j in zip(arr1,arr2)]
    for i in arr :
        s = ""
        for j in range(n) :
            s += "#" if i & (1 << (n-j-1)) else " "
        answer.append(s)
    return answer
