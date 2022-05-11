# def solution(sizes):
#     answer = 0
#     w, h = [],[]
#     for size in sizes:
#         w.append(min(size))
#         h.append(max(size))
#     answer = max(w)*max(h)
#     return answer


# def solution(sizes):
#     answer = 0
#     r, c = 0, 0
#     for w,h in sizes:
#         r = max((h if w>h else w), r)
#         c = max((h if w<h else w), c)
    
#     return r*c

def solution(sizes):
    answer = 0
    r, c = 0, 0
    for w,h in sizes:
        big, small = (w,h) if w>h else (h,w)
        r = big if big > r else r
        c = small if small > c else c
    
    return r*c
