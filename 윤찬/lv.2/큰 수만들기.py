def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)
    if k > 0:
        for i in range(k):
            stack.pop()
    return ''.join(stack)
