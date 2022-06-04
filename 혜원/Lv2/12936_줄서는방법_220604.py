def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

def solution(n, k):
    answer = [] 
    nums = [i for i in range(1,n+1)]
    for i in range(1, n+1):
        q, k = divmod(k, fact(n-i))
        if k == 0:
            answer.append(nums.pop(q-1))            
            break            
        else:
            answer.append(nums.pop(q))            
        

    while nums:
        answer.append(nums.pop())
    print(answer)

    return answer
