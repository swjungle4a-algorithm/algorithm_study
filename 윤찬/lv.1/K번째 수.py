def solution(array, commands):
    answer = []
    for start, end, idx in commands:
        answer.append(sorted(array[start-1:end])[idx-1])
    return answer
