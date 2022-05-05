from collections import deque
import re

def solution(dartResult):
    answer = []
    q = []
    flag = True
    i = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] == "1" and dartResult[i+1] == "0":
            q.append(10)
            flag = False
            continue
            
        elif dartResult[i].isnumeric() and flag:
            if not flag and dartResult[i] == "0":
                flag = True
                continue
                
            q.append(int(dartResult[i]))

    result = list(filter(lambda x : x , re.split('[^SDT*#]{1}', dartResult)))
    
    for num, operator in zip (q, result):
        tmp = num
        cnt = 0
        for op in operator:
            if op == "S":
                tmp = num
                
            elif op == "D":
                tmp = num**2
            
            elif op == "T":
                tmp = num**3
                
            elif op == "*":
                if answer:
                    tmp = (2 * tmp)
                    answer[-1] *= 2
                    
                else:
                    tmp *= 2
            
            elif op == "#":
                cnt -= 1
        
        answer.append(tmp*cnt if cnt else tmp)

    return sum(answer)
