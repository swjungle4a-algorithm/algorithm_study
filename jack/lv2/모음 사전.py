vowels = {"A" : 1, "E" : 2, "I" : 3, "O" : 4, "U" : 5}

def find(w):
    lv = [781, 156, 31, 6, 1]
    rst = 0
    for i in range(len(w)) :
        rst += (vowels[w[i]] - 1) * lv[i] + 1
    return rst

def solution(word):
    answer = find(word)
    return answer
