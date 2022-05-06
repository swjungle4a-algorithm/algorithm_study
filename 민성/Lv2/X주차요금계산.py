def solution(fees, records):
    answer = []
    
    base_min, base_coin,minute,minute_cost = fees
        
    record = []
    in_car = []
    out_car = []
    
    for tmp in records:
        tmp2 = tmp.split()
        if tmp2[2] == 'IN':
            in_car.append(tmp2)
        else:
            out_car.append(tmp2)

    for out in out_car:
        target_hour, target_min = out[0].split(':')
        
        target_time = int(target_hour) * 60 + int(target_min)
        target_num = out[1]
        
        for idx,car in enumerate(in_car):
            
            target_hour, target_min = car[0].split(':')
            in_time = int(target_hour) * 60 + int(target_min)
            
            in_num = car[1]
            
            if in_num == target_num:
                cost = target_time - in_time
                print(cost)
                flag=True
                for i in range(len(record)):
                    if record[i][0] == in_num:
                        record[i][1] += cost
                        flag=False
                if flag:
                    record.append([in_num,cost])
                    
                del in_car[idx]
                break
                
    while in_car:

    print(record)
    return answer
