def solution(dartResult):
    score = {'S':1, 'D':2, 'T':3}
    result = []
    sc = ''
    for s in dartResult:
        if s.isdigit():
            sc += s
        else:
            if sc:
                result.append(int(sc))
                sc = ''
            length = len(result)-1
            if s in score:
                result[length] = result[length] ** score[s]
            else:
                if s == '*':
                    if length > 0:
                        result[length] *= 2
                        result[length-1] *= 2
                    else:
                        result[length] *= 2
                elif s == '#':
                    result[length] *= -1
                
    return sum(result)
