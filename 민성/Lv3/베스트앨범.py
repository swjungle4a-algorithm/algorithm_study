from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    dicts=defaultdict(list)
    best_genre = defaultdict(int)
    
    for idx, album in enumerate(zip(genres, plays)):
        dicts[album[0]].append((idx, album[1]))
        best_genre[album[0]] += album[1]
    
    best = sorted(dicts.keys(), key=lambda x:sum(dicts[x][1]), reverse=True)

    for genre in best:    
        dicts[genre].sort(key=lambda x : x[1], reverse=True)
        if len(dicts[genre]) == 1:
            answer.append(dicts[genre][0][0])
            continue
        else:
            a = dicts[genre][0][1]
            b = dicts[genre][1][1]
            idx_a = dicts[genre][0][0]
            idx_b = dicts[genre][1][0]
            if a == b:  
                if idx_a < idx_b:
                    answer.append(idx_a)
                    answer.append(idx_b)
                else:
                    answer.append(idx_b)
                    answer.append(idx_a)
            else:
                answer.append(idx_a)
                answer.append(idx_b)
    return answer
