def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            left_gap = {2:{1: 1, 2: 0, 4: 2, 5: 1, 7: 3, 8: 2, 0: 3, '*': 4},
                  5:{1: 2, 2: 1, 4: 1, 5: 0, 7: 2, 8: 1, 0: 2, '*': 3},
                  8:{1: 3, 2: 2, 4: 2, 5: 1, 7: 1, 8: 0, 0: 1, '*': 2},
                  0:{1: 4, 2: 3, 4: 3, 5: 2, 7: 2, 8: 1, 0: 0, '*': 1}}
            right_gap = {2:{2: 0, 3: 1, 5: 1, 6: 2, 8:2, 9: 3, 0: 3, '#': 4},
                  5:{2: 1, 3: 2, 5: 0, 6: 1, 8: 1, 9: 2, 0: 2, '#': 3},
                  8:{2: 2, 3: 3, 5: 1, 6: 2, 8: 0, 9: 1, 0: 1, '#': 2},
                  0:{2: 3, 3: 4, 5: 2, 6: 3, 8: 1, 9: 2, 0: 0, '#': 1}}
       
            if left_gap[num][left] < right_gap[num][right]:
                answer += 'L'
                left = num
            elif left_gap[num][left] > right_gap[num][right]:
                answer += 'R'
                right = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num                    
                else:
                    answer += 'R'
                    right = num

    return answer
