from collections import defaultdict
def solution(dartResult):
    answer = [0] * 10
    
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    bonus = defaultdict(int);bonus['S'] = 1;bonus['D'] = 2;bonus['T'] = 3 
    
    index = 0
    flag = False
    for idx, val in enumerate(dartResult):
        if flag:
            flag = False
            continue
        if val == '1':
            if dartResult[idx+1] == '0':
                flag = True
                index += 1
                answer[index] = 10
                continue
        
        if val in number:    
            if index == 0 and idx > 0:
                index+=1
                answer[index] = int(val)
                continue
            if index == 0:
                answer[index] = int(val)
                continue
                
            index+=1
            answer[index] = int(val)
            
        if val == '*':
            answer[index] *= 2
            if index != 0:
                answer[index-1] = answer[index-1] * 2
            
        if val == '#':
            answer[index] *= -1

        if val == 'S' or val == 'D' or val == 'T':       
            answer[index] = answer[index]**bonus[val]

    return sum(answer)
