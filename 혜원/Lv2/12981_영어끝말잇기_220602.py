def solution(n, words):
    answered = []
    keyword = words[0][0]
    for i, word in enumerate(words):
        if keyword != word[0] or word in answered or len(word) < 2:
            return [i%n+1, i//n+1]
        answered.append(word)
        keyword = word[-1]
    return [0,0]
