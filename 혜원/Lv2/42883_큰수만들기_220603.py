def solution(number, k):
    # answer = ''
    # number = list(number)
    cnt = 0
    i = 0
    # print(dir(number))
    while k:
        if i == len(number)-1:
            break
        if number[i] < number[i+1]:
            number = number[:i]+number[i+1:]
            k -= 1
            if i != 0: i-=1
        else:
            i += 1
    while k:
        number = number[:-1]
        k-=1
    return number
