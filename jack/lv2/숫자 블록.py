def check(n) :
    if n == 1 : 
        return 0
    limit = int(n ** 0.5)
    x = 2
    for x in range(2, limit + 1) :
        if n % x == 0 and n // x <= 10000000 :
            break
    else : x = n
    return n//x

solution = lambda begin, end : [check(x) for x in range(begin, end+1)]
