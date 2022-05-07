def solution(s):    
    dic = {'zero' : "0", 'one' : "1", 'two' : "2", 'three' : "3", 'four' : "4", 'five' : "5", 'six' : "6", 'seven' : "7", 'eight' : "8", 'nine' : "9"}

    for d in dic.keys():
        if d in s:
            s = s.replace(d, str(dic[d]))
    
    return int(s)
