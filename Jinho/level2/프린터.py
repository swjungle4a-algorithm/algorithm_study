from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    index = deque([0] * len(priorities))
    index[location] = 1
    priorities.sort(reverse=True)
    while True:
        if q[0] == priorities[answer]:
            answer += 1
            if index[0]: break
            q.popleft()
            index.popleft()
        else:
            q.rotate(-1)
            index.rotate(-1)
    return answer
