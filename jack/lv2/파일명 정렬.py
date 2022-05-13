import re

def solution(files):
    answer = []
    
    tmp = []
    for file in files :
        f = []
        f.append(re.search('^[A-Za-z- .]+', file).group())
        f.append(re.search('\d+', file).group())
        if (t := ''.join(f)) != file :
            f.append(file[len(t):])
        tmp.append(f)
    
    tmp.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for t in tmp :
        answer.append(''.join(t))
    return answer
