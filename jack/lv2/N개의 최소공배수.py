from math import gcd

def lcm(a, b) :
    return a * b // gcd(a,b)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer,arr[i])
    return answer
