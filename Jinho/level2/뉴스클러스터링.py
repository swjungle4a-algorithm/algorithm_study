from collections import Counter

def solution(str1, str2):
    answer = 0
    str11 = []
    str22 = []
    
    tmp = ''
    str1 = str1.lower()
    str2 = str2.lower()
    
    for s in str1:
        if s.isalpha():
            tmp += s
            if len(tmp) == 2:
                str11.append(tmp)
                tmp = str(s)
        else:
            tmp = ''
                
    tmp =''
    for s in str2:
        if s.isalpha():
            tmp += s
            if len(tmp) == 2:
                str22.append(tmp)
                tmp = str(s)
        else:
            tmp = ''
                
    
    a = Counter(str11)
    b = Counter(str22)
    
    c = a & b
    d = a | b
    
    print(c)
    
    sum1 = 0
    sum2 = 0
    
    for key in c:
        sum1 += c[key]
    for key in d:
        sum2 += d[key]
        
    if sum2:
        return int(sum1/sum2*65536)
    else:
        return 65536
    
