import math
def solution(fees, records):
    answer = []
    
    time_a, fee_a, time_b, fee_b = fees

    carInfo = {}
    
    for s in records:
        time, car, inout = s.split(' ')
        car = int(car)
        time = time.split(':')
        t1 = int(time[0])
        t2 = int(time[1])
        
        if car not in carInfo:
            carInfo[car] = [(t1*60+t2, inout)]
        else:
            carInfo[car].append((t1*60+t2, inout))
    
    last = 23 * 60 + 59
    
    
    
    for item in carInfo.items():
        t = 0
        carnum = item[0]
        record = item[1]
        if record[-1][1] == 'IN':
            record.append((last, 'OUT'))
        for a, b in record:
            
            if b == 'OUT':
                t += a
            else:
                t -= a
        
                
        fee_now = fee_a + math.ceil((t-time_a)/time_b) * fee_b
        
        if t < time_a:
            fee_now = fee_a
        
        
        answer.append(fee_now)
    
    print(answer)

    return answer
