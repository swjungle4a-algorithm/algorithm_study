def solution(s, n):
    
    answer = ''
    # answer = s.replace([a-z,A-Z], )
    ch = ''
    for tmp in map(ord, s):
        print('tmp :', tmp)
        if tmp == 32:
            ch = 32
        else:
            ch = tmp+n
            if 97<=tmp<=122:
                # ch = (ch-96)%26 + 96
                if ch>122: ch = ch-122+96
            elif 65<=tmp<=90:
                # ch = (ch-64)%26 + 64
                if ch>90: ch = ch-90+64
            print(tmp, ch)
            
            # answer += chr(ch) if 97<ch<122 or 65<ch<90 else chr(ch-26)
        answer += chr(ch)
        
    # print(ord('a'), ord('A'), ord('z'), ord('Z'))
    # print(chr(97))
    return answer
