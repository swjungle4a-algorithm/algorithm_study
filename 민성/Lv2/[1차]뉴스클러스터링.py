from collections import Counter
def solution(str1, str2):
    answer = 0
    
    lower_str1 = str1.lower()
    lower_str2 = str2.lower()
    
    list_str1 = []
    list_str2 = []
    
    for i in range(len(lower_str1)-1):
        if lower_str1[i].isalpha() and lower_str1[i+1].isalpha():
            list_str1.append(lower_str1[i] + lower_str1[i+1])
            
    for i in range(len(lower_str2)-1):
        if lower_str2[i].isalpha() and lower_str2[i+1].isalpha():
            list_str2.append(lower_str2[i] + lower_str2[i+1])

    
    counter_str1 = Counter(list_str1)
    counter_str2 = Counter(list_str2)

    inter = list((counter_str1 & counter_str2).elements())
    union = list((counter_str1 | counter_str2).elements())
    
    if not len(inter) and not len(union):
        answer = 65536
    else:
        answer = int(len(inter) / len(union) * 65536)
    
    
    return answer
