def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        answer.append(bin(a|b)[2:].rjust(n, "0").replace("1", "#").replace("0", " "))
                     
    return answer
