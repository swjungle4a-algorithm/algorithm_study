def solution(sizes):
    left = []
    right = []
    for square in sizes:
        left.append(max(square))
        right.append(min(square))
    return max(left) * max(right)
