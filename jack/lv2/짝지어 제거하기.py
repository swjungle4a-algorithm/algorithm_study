def solution(s):
    answer = 0
    stk = []

    for c in s:
        if stk and stk[-1] == c:
            stk.pop()
            continue

        stk.append(c)

    answer = 0 if stk else 1

    return answer
