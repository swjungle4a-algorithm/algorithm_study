from math import factorial

def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    k -= 1

    for i in range(n-1, -1, -1):
        q, k = divmod(k, factorial(i))
        answer.append(nums.pop(q))
    
    return answer
