from collections import deque

class Bridge :
    def __init__(self, bridge_length) :
        self.que = [0 for _ in range(bridge_length)]
        self.length = bridge_length
        self.front = 0
        self.rear = bridge_length - 1
        self.weight = 0
        self.count = 0
    
    def flow(self) :
        self.count -= 1 if self.que[self.front] else 0
        self.weight -= self.que[self.front]
        self.que[self.front] = 0
        self.front = (self.front + 1) % self.length
        self.rear = (self.rear + 1) % self.length
        
    def push(self, truck) :
        self.que[self.rear] = truck
        self.weight += truck
        self.count += 1
    

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    brg = Bridge(bridge_length)    
    sec = 1
    while trucks :
        if brg.count <= bridge_length and brg.weight + trucks[0] <= weight :
            brg.push(trucks.popleft())
        brg.flow()
        sec += 1
    
    while brg.count :
        sec += 1
        brg.flow()
    answer = sec
    return answer
