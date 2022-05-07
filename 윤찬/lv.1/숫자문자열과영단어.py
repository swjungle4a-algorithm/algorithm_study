from re import sub
def solution(s):    
    s = sub('zero', '0', s)
    s = sub('one', '1', s)
    s = sub('two', '2', s)
    s = sub('three', '3', s)
    s = sub('four', '4', s)
    s = sub('five', '5', s)
    s = sub('six', '6', s)
    s = sub('seven', '7', s)
    s = sub('eight', '8', s)
    s = sub('nine', '9', s)
    return int(s)
