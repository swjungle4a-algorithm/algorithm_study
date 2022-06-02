def div(p):
    cnt = 0
    for i, v in enumerate(p):
        if v == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:i+1], p[i+1:]


def check(u):
    cnt = 0
    for i in u:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def solution(p):
    # pass 1
    if not p:    
        return ""

    # pass 2
    u, v = div(p)
    
    # pass 3
    if check(u):
        # pass 3-1
        return u + solution(v)
    
    # pass 4
    else:
        # pass 4-1, 4-2, 4-3
        answer = "(" + solution(v) + ")"
        
        # pass 4-4
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        
        # pass 4-5
        return answer
