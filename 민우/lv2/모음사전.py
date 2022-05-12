from itertools import product

def solution(word):
    answer = ['0']
    
    for i in range(1, 6):
        answer.extend(list(map("".join, product("AEIOU", repeat = i))))

    return sorted(answer).index(word)
