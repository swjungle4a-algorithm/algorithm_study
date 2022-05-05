def solution(dartResult):
    answer = 0
    temp = ''
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    stack = []
    stack_a = []

    for str in dartResult:
        if str in arr:
            temp += str
        else:
            if str == 'S':
                stack.append(int(temp)**1)
            elif str == 'D':
                stack.append(int(temp)**2)
            elif str == 'T':
                stack.append(int(temp)**3)
            elif str == '*':
                while stack:
                    stack_a.append(stack.pop() * 2)
            else:
                if stack:
                    answer -= stack.pop()
            print(stack)
            print(answer)
            temp = ''
    while stack:
        answer += stack.pop()

    return answer
