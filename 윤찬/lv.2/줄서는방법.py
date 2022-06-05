from math import factorial
def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    for i in range(1, n+1):
        index, k = divmod(k, factorial(n-i))
        answer.append(arr.pop(index-1)) if k == 0 else answer.append(arr.pop(index))
    return answer
