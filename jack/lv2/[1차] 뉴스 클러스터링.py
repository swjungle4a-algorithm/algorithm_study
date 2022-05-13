from collections import Counter
import re

# 비트연산 없이 푼 버전
def J(A, B) :
    if len(A) == 0 and len(B) == 0 :
        return 65536
    rst = 0
    sum = Counter(A+B)
    A = Counter(A)
    B = Counter(B)
    len_sum = 0
    len_gyo = 0
    
    for a, b in sum.most_common() :
        len_sum += max(A[a], B[a])
        len_gyo += min(A[a], B[a])
    
    
    rst = len_gyo / len_sum
    return int(rst * 65536)

# 비트연산으로 푼 버전
def J_bit(A, B) :
    if len(A) == 0 and len(B) == 0 :
        return 65536
    rst = 0
    len_sum = len_gyo = 0
    
    dict_sum = Counter(A) | Counter(B)
    for key in dict_sum :
        len_sum += dict_sum[key]
    dict_gyo = Counter(A) & Counter(B)
    for key in dict_gyo :
        len_gyo += dict_gyo[key] 
        
    rst = len_gyo / len_sum
    return int(rst * 65536)
    

def solution(str1, str2):
    answer = 0
    str1 = re.sub('[^a-z]', ' ', str1.lower())
    str2 = re.sub('[^a-z]', ' ', str2.lower())
    A = []
    B = []
    for i in range(len(str1)-1) :
        if " " not in str1[i:i+2] :
            A.append(str1[i:i+2])
    for i in range(len(str2)-1) :
        if " " not in str2[i:i+2] :
            B.append(str2[i:i+2])

    answer = J_bit(A, B)
    return answer
