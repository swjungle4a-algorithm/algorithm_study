def solution(n, words):
    word_set = []
    cnt = 0
    for i, word in enumerate(words, 1):
        if i % n == 1:
            cnt += 1
        if word_set and (word in word_set or word_set[-1][-1] != word[0]):
            if i % n == 0:
                return [n, cnt]
            else:
                return [i%n, cnt]    
        word_set.append(word)
    else:
        return [0, 0]
