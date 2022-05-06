from math import ceil


def solution(fees, records):
    answer = []
    q = []

    for idx, record in enumerate(records):
        time, number, status = record.split()
        hour, minute = time.split(':')
        records[idx] = [number, int(hour) * 60 + int(minute), status]
    records.sort()
    print(*records, sep='\n')

    timeIn = timeOut = timeTot = 0
    numCar = ""
    flag = False

    for record in records:
        num, time, status = record
        if num != numCar:
            if flag:
                timeTot += 1439 - timeIn
                flag ^= True
            if timeTot:
                if timeTot <= fees[0]:
                    answer.append(fees[1])
                else:
                    feeTot = fees[1] + \
                        ceil((timeTot - fees[0]) / fees[2]) * fees[3]
                    answer.append(feeTot)
            numCar = num
            timeIn = time
            timeTot = 0
            flag ^= True
            continue

        if status == "IN":
            timeIn = time
            flag ^= True
        else:
            timeTot += time - timeIn
            flag ^= True
    if flag:
        timeTot += 1439 - timeIn
    if timeTot <= fees[0]:
        answer.append(fees[1])
    else:
        feeTot = fees[1] + ceil((timeTot - fees[0]) / fees[2]) * fees[3]
        answer.append(feeTot)
    return answer
