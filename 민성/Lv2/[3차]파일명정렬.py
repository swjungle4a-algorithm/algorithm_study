import re
def solution(files):
    dicts = []
    head = re.compile('[^0-9]+')
    number = re.compile('[0-9]+')
    for i in range(len(files)):
        head_search = re.search(head, files[i])
        number_search = re.search(number, files[i])
        
        dicts.append([files[i], head_search[0], number_search[0]])
        
    dicts.sort(key=lambda x:(x[1].lower(), int(x[2])))
    
    return [i[0] for i in dicts]
