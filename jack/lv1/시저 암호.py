def solution(s, n):
    answer = ''
    for char in s :
        if char == " " :
            answer += char
            continue
        c = ord(char)
        if c <= 90 :
            answer += chr(((c-65) + n) % 26 + 65)
        else :
            answer += chr(((c-97) + n) % 26 + 97)
    return answer
