def solution(s, n):
    answer = ''

    for char in s:
        if char == ' ':
            answer += ' '
            continue
        num_ord = ord(char)

        if 97<=num_ord<=122:
            num_ord += n
            if num_ord >122:
                num_ord-=26
        else:
            num_ord += n
            if num_ord >90:
                num_ord-=26
        answer+=chr(num_ord)
        
    return answer
