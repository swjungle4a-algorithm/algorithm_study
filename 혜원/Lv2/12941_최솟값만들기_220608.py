def solution(A,B):
    return answer = sum([a*b for a,b in zip(sorted(A), sorted(B, reverse=True))])

  
################################  
#     answer = 0
#    
#     A.sort()
#     B.sort(reverse = True)
#    
#     for a, b in zip(A, B):
#         answer += a*b
