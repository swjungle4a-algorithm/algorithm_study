def solution(s, n):
    answer = ''
    for i in s:
        tmp = ord(i)
        if 97 <= tmp <= 122:
            tmp += n
            if tmp > 122:
                tmp -= 26
        elif 65 <= tmp <= 90:
            tmp += n
            if tmp > 90:
                tmp -= 26
        answer += chr(tmp)
    return answer
