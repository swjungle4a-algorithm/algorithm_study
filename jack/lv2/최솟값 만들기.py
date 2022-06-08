solution = lambda A, B : sum(map(lambda x: x[0] * x[1], zip(sorted(A),sorted(B, reverse=True))))
