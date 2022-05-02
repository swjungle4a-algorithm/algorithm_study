```python
import re

def solution(new_id):
    answer = ''
    
    # pass 1
    answer = new_id.lower()
    
    # pass 2
    answer = re.sub("[^a-z0-9\-_.]","",answer)
    
    # pass 3
    answer = re.sub("[..]+", ".", answer)
    
    # pass 4
    answer = re.sub("^[.]", "", answer)
    
    # pass 5
    answer = "a" if not answer else answer
    
    # pass 6
    answer = re.sub("^[.]|[.]$", "", answer[:15]) if len(answer) >= 16 else re.sub("^[.]|[.]$", "", answer)
    
    # pass 7
    answer = answer + answer[-1] * (3-len(answer)) if len(answer) <= 2 else answer
    
    return answer
```
