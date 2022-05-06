from math import ceil

def solution(fees, records):
    answer = []

    car_dict = {}

    basic_time = fees[0]
    basic_cost = fees[1]
    unit_time = fees[2]
    unit_cost = fees[3]

    max_min = 23 * 60 + 59

    for record in records:
        temp = record.split()
        car_time = list(map(int, temp[0].split(':')))
        car_num = int(temp[1])
        car_status = temp[2]

        car_hour = car_time[0]
        car_min = car_time[1]
        total_min = car_hour * 60 + car_min

        if car_num not in car_dict:
            car_dict[car_num] = [0, 0]

        if car_status == 'IN':
            car_dict[car_num][0] -= total_min
        else:
            car_dict[car_num][0] += total_min

        car_dict[car_num][1] += 1

    for i in car_dict:
        if car_dict[i][1] % 2 == 1:
            car_dict[i][0] += max_min
        car_dict[i][0] -= basic_time
        car_dict[i][0] = 0 if car_dict[i][0] < 0 else car_dict[i][0]
        car_dict[i][0] = basic_cost + \
            ceil(car_dict[i][0] / unit_time) * unit_cost

    for i in sorted(car_dict.keys()):
        answer.append(car_dict[i][0])

    return answer