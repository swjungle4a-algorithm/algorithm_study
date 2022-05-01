from math import ceil

def car_time(dict):
    result = [0] * len(dict)
    idx = 0

    for car_num in dict:
        temp = dict[car_num]
        size = len(temp)
        for record in temp:
            record_s = record.split()
            minute = record_s[0]
            status = record_s[2]
            hm = list(map(int, minute.split(':')))

            if status == 'IN':
                result[1] -= (hm[0] * 60) + hm[1]
            else:
                result[1] += (hm[0] * 60) + hm[1]
        if size % 2 == 1:
            result[1] += (23 * 60) + 59

        idx += 1
    return result

def car_records(fees, records):
    a = fees[0]
    b = fees[1]
    c = fees[2]
    d = fees[3]

    result = []
    dict = {}
    for record in records:
        temp = record.split()
        car_num = temp[1]
        if car_num in dict:
            dict[car_num] += [record]
        else:
            dict[car_num] = [record]

    for i in car_time(dict):
        e = i - a if i - a > 0 else 0
        temp = b + (ceil(e / c) * d)
        result.append(temp)
    return result

def solution(fees, records):
    answer = []
    answer = car_records(fees, records)
    return answer
