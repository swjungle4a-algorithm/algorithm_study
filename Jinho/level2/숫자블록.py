def solution(begin, end):
    answer = []
    block_list = range(begin, end+1)
    for num in block_list:
        lim = int(num**0.5)
        for d in range(2, lim+1):
            if num % d == 0 and num//d < 10000001:
                answer.append(num//d)
                break
        else:
            answer.append(1)
    if begin == 1:
        answer[0] = 0
    return answer
