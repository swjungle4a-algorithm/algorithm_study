from collections import Counter

def solution(nums):
    answer = 0
    need = len(nums) // 2
    c = len(set(nums))
    answer = need if c >= need else c
    return answer
