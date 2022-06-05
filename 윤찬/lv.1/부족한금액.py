def solution(price, money, count):
    answer = -1
    s = 0
    for i in range(1, count+1):
        s += price * i
    return 0 if s-money <=0 else s-money
