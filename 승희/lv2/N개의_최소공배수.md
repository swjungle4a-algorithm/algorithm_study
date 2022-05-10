```python3
import math

def solution(arr):
    answer = 1
    
    n = len(arr)
    for i in range(n):
        gcd = math.gcd(arr[i], answer)
        answer *= arr[i]
        answer //= gcd

    return answer
```
