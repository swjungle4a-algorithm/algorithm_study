from collections import deque
def solution(priorities, location):
    tmp = []
    for i in range(len(priorities)):
        tmp.append([priorities[i], i])
    tmp.sort(reverse=True, key=lambda x: x[0])
    # for val, idx in tmp:
    #     if l
    print(tmp)
    return 0
