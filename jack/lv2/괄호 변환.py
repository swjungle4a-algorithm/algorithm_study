def convert(u) :
    if not u : return u
    a, b = split(u)
    if check(a) : 
        b = convert(b)
        a = a + b
        return a
    s = "("
    s += convert(b)
    s += ")"
    a = a[1:len(a)-1] if len(a) > 2 else ""
    a = a.replace("(","}").replace(")","(").replace("}",")")
    s += a
    return s
    
def check(u) :
    cnt = 0
    for c in u :
        cnt += 1 if c == "(" else -1
        if cnt < 0 :
            return 0
    return 1

def split(w) :
    u = ""
    v = ""
    chk = 0
    
    for c in w :
        chk += 1 if c == "(" else -1
        u += c
        if not chk :
            break
    
    v = w[len(u):]
    return u, v

def solution(p):
    if check(p) : return p
    answer = convert(p)
    return answer
