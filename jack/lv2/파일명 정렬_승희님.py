import re

def solution(files):
    answer = []
    for file in files:
        head = re.search('^[^0-9]+', file).group().lower()
        number = int(re.search('[0-9]+', file).group())
        # print(head, number)
        answer.append([head, number, file])

    answer.sort(key=lambda x:x[1])
    answer.sort(key=lambda x:x[0])

    result = []
    for x in answer:
        result.append(x[2])

    return result
