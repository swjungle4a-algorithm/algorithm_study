from collections import Counter
import re

def solution(str1, str2):
    answer = ""
    str1 = str1.lower()
    str2 = str2.lower()

    if str1 == str2:
        return 65536
    
    l1 = []
    l2 = []
    
    for i in range(1, len(str1)):
        tmp = ""
        if str1[i-1].isalpha() and str1[i].isalpha():
            tmp = str1[i-1] + str1[i]
        else:
            continue
        l1.append(tmp)
        
    for i in range(1, len(str2)):
        tmp = ""
        if str2[i-1].isalpha() and str2[i].isalpha():
            tmp = str2[i-1] + str2[i]
        else:
            continue
        l2.append(tmp)
            
    d1 = Counter(l1)
    d2 = Counter(l2)
    
    a = 0
    for com in (d1 & d2):
        a += (d1 & d2)[com]
        
    b = 0
    for uni in (d1 | d2):
        b += (d1|d2)[uni]
    
    answer = int(a / b * 65536)

    return answer
