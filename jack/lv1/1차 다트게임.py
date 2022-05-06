def solution(dartResult):
    answer = 0
    cal = [0, 0, 0]
    area = {"S" : 1, "D" : 2, "T" : 3}
    
    
    idx = 0
    for i, rst in enumerate(dartResult) :
        try :
            if int(rst) == 0 and (i>0 and int(dartResult[i-1] == "1")) :
                continue
            if rst == "1" and dartResult[i+1] == "0" :
                cal[idx] = 10
            else :
                cal[idx] = int(rst)
            idx += 1
        except :
            if rst in area.keys() :
                cal[idx-1] = cal[idx-1] ** area[rst]
            else :
                if rst == "*" :
                    if idx-1 > 0 :
                        cal[idx-2] *= 2
                    cal[idx-1] *= 2
                elif rst == "#" :
                    cal[idx-1] = -cal[idx-1]
    answer = sum(cal)
    return answer
