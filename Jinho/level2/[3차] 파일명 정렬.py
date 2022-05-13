def solution(files):
    answer = []
    print(files)
    for filename in files:
        tmp = []
        for i, s in enumerate(filename):
            length = len(filename)
            if s.isdigit() and not tmp:
                tmp.append(filename[:i])
            elif tmp and not s.isdigit():
                tmp.append(filename[len(tmp[0]):i])
                tmp.append(filename[i:])
                answer.append(tmp)
                break
        else:
            tmp.append(filename[len(tmp[0]):])
            answer.append(tmp)
                
    
    print("answer:", answer)
    answer.sort(key = lambda x:int(x[1]))
    answer.sort(key = lambda x:x[0].upper())
    
    answer2 = []
    
    for s in answer:
        answer2.append(''.join(s))
        
    print(answer2)
    
    return answer2
