import re
def solution(numbers):
    answer = []
    for num in numbers:
        tmp = num
        if num % 2 == 0:
            answer.append(num+1)
        else:
            for i in range(1, 50):
                if (1<<i) & num != (1<<i):
                    tmp = num - (1<<i-1)
                    j = i+1
                    while((1<<j) < num):
                        tmp |= (1<<j)
                        j += 1
                    tmp |= (1<<i)
                    num |= (1<<i)
                    num &= tmp
                    answer.append(num)
                    break;
    return answer
