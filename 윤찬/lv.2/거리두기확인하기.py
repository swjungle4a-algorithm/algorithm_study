def solution(places):
    answer = []

    for place in places:
        p = [[] for _ in range(5)]
        x = [[] for _ in range(5)]

        for i in range(5):
            row = place[i]
            for j in range(5):
                status = row[j]
                if status == 'P':
                    p[i].append(j)
                elif status == 'X':
                    x[i].append(j)

        for i in range(5):
            if len(p[i]) == 0:
                continue

    return answer
