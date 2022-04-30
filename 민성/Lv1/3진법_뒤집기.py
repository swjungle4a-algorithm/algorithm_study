def solution(n):
    answer=0
    nums = []
    while(True):
        if n<3:
            nums.append(n)
            break
        nums.append(n%3)
        n = n // 3

    i=len(nums)-1
    for num in nums:
        if i == 0:
            answer+=num
            break  
        answer += 3**i*num
        i-=1
    
    return answer


def solution(n):
    tmp = ''
    while n:
        # tmp에 나머지들을 문자열형태로 저장하고
        tmp += str(n % 3)
        n = n // 3

    # int(str, n) 으로 n진법으로 10진수를 리턴할 수 있다.
    answer = int(tmp, 3)
    return answer
