from collections import defaultdict
def solution(genres, plays):
    answer = []
    result = defaultdict(list)
    tmp = []
    for genre, play in zip(genres, plays):
        result[genre].append((play, i))
    
    for i in result.items():
        i[1].sort(key=lambda x: x[1])
        result[i[0]] = sorted(i[1], reverse=True, key=lambda x: x[0])
        tmp.append([sum(list(map(lambda x: x[0], i[1]))), i[0]])

    for i in sorted(tmp, reverse=True, key=lambda x: x[0]):
        n = 0
        for j in result[i[1]]:
            n += 1
            answer.append(j[1])
            if n == 2: break

    return answer
