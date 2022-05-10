from re import sub
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = str(bin(arr1[i] | arr2[i]))
        tmp = sub("0b", "", tmp)
        if len(tmp) < n: tmp = "0"*(n - len(tmp)) + tmp
        tmp = sub("1", "#", tmp)
        tmp = sub("0", " ", tmp)
        answer.append(tmp)
    return answer
