def solution(numbers, hand):

    keypad = {'*':[0, 0], 0:[0,1], '#':[0,2],
             7:[1,0], 8:[1,1], 9:[1,2],
             4:[2,0], 5:[2,1], 6:[2,2],
             1:[3,0], 2:[3,1], 3:[3,2]}
    answer = ''
    left = [0, 0]
    right = [0, 2]
    for num in numbers:
        if num in [1, 4, 7]:
            left = keypad[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            right = keypad[num]
            answer += 'R'
        else:
            distLeft = abs(keypad[num][0] - left[0]) + abs(keypad[num][1] - left[1])
            distRight = abs(keypad[num][0] - right[0]) + abs(keypad[num][1] - right[1]) 
            if distLeft < distRight:
                left = keypad[num]
                answer += 'L'
            elif distLeft > distRight:
                right = keypad[num]
                answer += 'R'
            elif distLeft == distRight:
                if hand == 'right':
                    right = keypad[num]
                    answer += 'R'
                else:
                    left = keypad[num]
                    answer += 'L'
    
    return answer
