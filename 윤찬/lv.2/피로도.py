from itertools import permutations
def solution(k, dungeons):
    size = len(dungeons)
    answer = 0
    for permu in permutations(dungeons, size):
        tmp = 0
        tmpK = k
        for min_fatigue, use_fatigue in permu:
            if min_fatigue <= tmpK:
                tmpK -= use_fatigue
                tmp += 1
        answer = max(answer, tmp)
    return answer
