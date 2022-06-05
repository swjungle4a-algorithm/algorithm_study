def solution(array, commands):
    answer = []
    
    for com in commands:
        start = com[0]
        end = com[1]
        num = com[2]
        
        tmp = array[start-1:end]
        tmp.sort()
        answer.append(tmp[num-1])
    
    return answer
