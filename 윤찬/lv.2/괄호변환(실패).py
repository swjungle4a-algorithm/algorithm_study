def div_str(u, v, p):
    left = 0
    right = 0
    
    u.append(p[0])
    
    if p[0] == '(': left += 1 
    else: right += 1  
    
    for i in p[1:]:
        if left == right: 
            v.append(p[left + right - 1])
            break
        u.append(i)
    return u, v

def check(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if len(stack) > 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
    print(stack)
    # if stack[-2] == '(' and stack[-1] == ')':
    #     stack.pop()
    #     stack.pop()
    return True if len(stack) == 0 else False

def solution(p):
    if not p: return ''
    answer = ''
    u, v = div_str([], [], p)
    print(u, v)
    if check(u): answer += u
    return answer
