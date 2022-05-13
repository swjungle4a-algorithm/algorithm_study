def solution(s):
    nums = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    answer = ''
    tmp = ''
    for word in s:
        
        if word.isalpha(): 
            tmp += word
        else:
            answer += word
            continue
        if tmp and tmp in nums.keys():
            answer += str(nums[tmp])
            tmp = ''
        
    return int(answer)
