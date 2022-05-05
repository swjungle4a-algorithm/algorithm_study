import re

def solution(dartResult):
    answer = []
    q = []
    flag = True

    for i in range(len(dartResult)):
        if dartResult[i] == "1" and dartResult[i+1] == "0":
            q.append(10)
            flag = False
            continue

        elif dartResult[i].isnumeric():
            if not flag and dartResult[i] == "0":
                flag = True
                continue
                
            q.append(int(dartResult[i]))
        
        else: continue
        
    result = list(filter(lambda x : x , re.split('[^SDT*#]{1}', dartResult)))

    for num, operator in zip (q, result):
        for op in operator:
            if op == "S":
                num **= 1

            elif op == "D":
                num **= 2

            elif op == "T":
                num **= 3

            elif op == "*":
                num *= 2
                if answer:    
                    answer[-1] *= 2
                
            elif op == "#":
                num *= -1

        answer.append(num)

    return sum(answer)
