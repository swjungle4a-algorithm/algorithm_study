from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for dungeon in permutations(dungeons, len(dungeons)) :
        tmp_k = k
        count = 0
        for case in dungeon :
            min_fatigue, consume_fatigue = case
            if tmp_k >= min_fatigue :
                tmp_k -= consume_fatigue
                count += 1
        answer = max(answer, count)
        
    return answer
