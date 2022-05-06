from collections import Counter
from math import floor
from re import findall, compile


def arr_split(str):
    c = compile('[^a-z]')
    arr = []
    for i in range(len(str)-1):
        temp = str[i] + str[i+1]
        if c.findall(temp):
            continue
        arr.append(temp)
    return arr


def solution(str1, str2):
    A = arr_split(str1.lower())
    B = arr_split(str2.lower())

    a = Counter(A)
    b = Counter(B)

    inter = a & b
    union = a | b

    inter_cnt = 0
    union_cnt = 0

    for i in inter:
        inter_cnt += inter[i]

    for i in union:
        union_cnt += union[i]

    if inter_cnt == 0 and union_cnt == 0:
        return 65536
    else:
        return int(inter_cnt/union_cnt*65536)
