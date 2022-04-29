# 민우님꺼 참조한 코드

# 키패드 좌표 쓰기
keypad = {1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        0:(3,1)}

# 2,5,8,0 일 때 어느칸만큼 가야하는지 측정하기
def hand_cnt(num, loc):
    return abs(keypad[num][0] - loc[0]) + abs(keypad[num][1] - loc[1])


def solution(numbers, hand):
    answer = ""
    
    l_loc = (3,0)
    r_loc = (3,2)

    for num in numbers:

        if num in [1,4,7]:
            w_hand = 'left'
        elif num in [3,6,9]:
            w_hand = 'right'
        else:
            l_cnt = hand_cnt(num, l_loc)
            r_cnt = hand_cnt(num, r_loc)
            
            if l_cnt > r_cnt:
                w_hand = 'right'
            elif l_cnt < r_cnt:
                w_hand = 'left'
            else:
                w_hand = hand

        if w_hand == 'right':
            r_loc = keypad[num]
            answer+='R'
        else:
            l_loc = keypad[num]
            answer+='L'

    return answer
