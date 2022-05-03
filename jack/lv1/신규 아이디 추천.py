import re

def solution(new_id):
    answer = ''
    first = new_id.lower()
    m = re.compile(r'[a-z]*[0-9]*[-]*[_]*[.]*')
    second = ''.join(re.findall(m, first))
    m = re.compile(r'[.]?[\w,-,_]+')
    third = ''.join(re.findall(m, second))
    forth = third.strip('.')
    fifth = forth + "a" if forth == "" else forth
    sixth = fifth[:15]
    sixth = ''.join(re.findall(m, sixth)).strip('.')
    if len(sixth) < 3 :
        while len(sixth) != 3 :
            sixth += sixth[-1]
    seventh = sixth
    answer = seventh
    return answer
