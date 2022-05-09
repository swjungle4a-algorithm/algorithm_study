from re import match 
def solution(files):
    answer = []
    result = []
    for str in files:
        temp = match('[\sa-zA-Z-.]+', str)
        temp1 = match('[\sa-zA-Z-.]+[\d]+', str)
        answer.append([str[:temp.span()[1]]] + [str[temp.span()[1]:temp1.span()[1]]] + [str[temp1.span()[1]:]])
    answer.sort(key= lambda x: int(x[1]))
    answer.sort(key= lambda x: x[0].upper())
    for arr in answer:
        result.append("".join(arr))
    return result
