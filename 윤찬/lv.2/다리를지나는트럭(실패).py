from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    tmp = deque([0] * bridge_length)
    while queue:
        truck = queue.popleft()
        if tmp.count(0) == 0:
            tmp.popleft()
            answer += 1
        if sum(tmp) + truck <= weight:
            tmp.popleft()
            tmp.append(truck)
            answer += 1
        else:
            while sum(tmp) + truck > weight:
                tmp.popleft()
                answer += 1
                tmp.append(0)
            tmp.pop()
            tmp.append(truck)
            answer += 1
    while tmp:
        tmp.pop()
        answer += 1
    return answer
