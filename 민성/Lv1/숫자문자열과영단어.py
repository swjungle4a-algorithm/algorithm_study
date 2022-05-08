def solution(s):
    answer = []
    
    words = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    start = 0
    end = 1
    
    for idx, letter in enumerate(s):
        if letter.isdigit():
            answer.append(letter)
            start = idx+1
        else:
            end = idx
            try:
                answer.append(words[s[start:end+1]])
                start = idx+1
            except:
                continue
    answer = ''.join(answer)    
    return int(answer)          
