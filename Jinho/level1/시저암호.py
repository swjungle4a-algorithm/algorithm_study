def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            if i.lower() == i:
                answer += chr(97 + ((ord(i)-97) + n)%26)
            else:
                answer += chr(65 + ((ord(i)-65) + n)%26)
        else:
            answer += i
    return answer
