def solution(price, money, count):
    s = sum(range(1, count+1)) * price
    sub = s - money
    return sub if sub > 0 else 0
