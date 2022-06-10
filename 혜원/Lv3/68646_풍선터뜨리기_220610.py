def solution(a):
    answer = 0
    n = len(a)
    l_min, r_min = [],[]
    l, r = a[0], a[-1]
    for i in range(n):
        l = a[i] if a[i]<l else l
        l_min.append(l)
    for i in range(n-1, -1, -1):
        r = a[i] if a[i]<r else r
        r_min.append(r)
    for i in range(n):
        if l_min[i]<a[i] and r_min[n-(1+i)]<a[i]:
            continue
        else:
            answer+=1

    return answer
  
# ---------------------------------------
# ---------- 시간초과 ----------
#   def solution(a):
#     answer = 2
#     left, right, minimum = 0,0,min(a)
#     min_idx = a.index(minimum)
        
#     for i in range(1, len(a)-1):
#         if i<min_idx:
#             if a[i]<min(a[:i]) : answer += 1
#         elif i>min_idx:
#             if a[i]<min(a[i+1:]) : answer += 1
#         else:
#             answer+=1
                            
#     return answer
