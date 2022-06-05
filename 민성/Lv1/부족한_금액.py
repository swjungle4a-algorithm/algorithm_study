def solution(price, money, count):
    answer = -1

    total_money = (price + (price * count)) * count // 2

    if total_money <= money:
        answer = 0
    else:
        answer = total_money - money

    return answer
