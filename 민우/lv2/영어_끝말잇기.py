def solution(n, words):
    stack = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] in stack or words[i][0] != stack[-1][-1]:
            return [(i%n)+1, (i//n)+1]
        stack.append(words[i])
    
    return [0, 0]
