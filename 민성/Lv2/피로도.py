from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    order_dungeon = list(permutations(dungeons, len(dungeons)))
    
    for i in order_dungeon:
        tmp_ans = 0
        tmp_k = k
        for dungeon in i:
            min_stress = dungeon[0]
            down_stress = dungeon[1]
            
            if min_stress <= tmp_k:
                tmp_ans += 1
                tmp_k -= down_stress
            else:
                break
        if tmp_ans > answer:
            answer = tmp_ans
    
    return answer
