def solution(new_id):
    
    new_id = new_id.lower()
    string = ['-', '_', '.']
    answer = ''
    for s in new_id:
        if s in string or s.isdigit() or s.isalpha():
            answer += s
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer2 = ''
    length = len(answer) - 1
    
    for i, s in enumerate(answer):
        if (i==0 and s=='.') or (i==length and s =='.'):
            pass
        else:
            answer2 += s
    
    if answer2 == '':
        answer2 = 'a'
    
    if len(answer2) >= 16:
        answer2 = answer2[:15]
    if answer2[-1] == '.':
        answer2 = answer2[:14]
            
    length = len(answer2)
    
    while length <= 2:
        answer2 += answer2[-1]
        length += 1
        
    print(answer2)
    
    return answer2
