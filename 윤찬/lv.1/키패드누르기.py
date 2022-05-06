def solution(numbers, hand):
    answer = ''
    left_start = '*'
    right_start = '#'

    d = {0: [3, 2, 1, 0], 1: [1, 2, 3, 4], 2: [0, 1, 2, 3], 3: [1, 2, 3, 4], 4: [2, 1, 2, 3],
            5: [1, 0, 1, 2], 6: [2, 1, 2, 3], 7: [3, 2, 1, 2], 8: [2, 1, 0, 1], 9: [3, 2, 1, 2],
            '#': [4, 3, 2, 1], '*': [4, 3, 2, 1]}

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_start = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_start = i
        else:
            idx = 0
            left_dict = 0
            right_dict = 0

            if i == 2:
                idx = 0
            elif i == 5:
                idx = 1
            elif i == 8:
                idx = 2
            elif i == 0:
                idx = 3

            left_dict = d[left_start][idx]
            right_dict = d[right_start][idx]

            if left_dict == right_dict:
                if hand == 'right':
                    answer += 'R'
                    right_start = i
                else:
                    answer += 'L'
                    left_start = i
            elif left_dict > right_dict:
                answer += 'R'
                right_start = i
            else:
                answer += 'L'
                left_start = i

    return answer
