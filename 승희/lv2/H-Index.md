```python3
import bisect
def solution(citations):
    h = 0
    n = len(citations)
    
    citations.sort()
    print(citations)

    for x in range(citations[-1], -1, -1):
        h = x
        up = n - bisect.bisect_left(citations, x)
        down = bisect.bisect_left(citations, x)
        print(x, up, down)
        if up >= h and down <= h:
            break
    
    return h
```
