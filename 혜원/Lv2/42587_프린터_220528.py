# from queue import popleft, append, deque
from queue import deque
def solution(priorities, location):
    answer = 0
    dq = deque()
    for idx, priority in enumerate(priorities):
        dq.append((priority, idx))
    print(dq)
    while dq:
        prio, idx = dq.popleft()
        if prio == 0: continue
        if prio < max(priorities):
            dq.append((prio, idx))
        else:
            priorities[idx] = 0
            answer += 1
            if idx == location: break
            else: continue
        
    return answer
