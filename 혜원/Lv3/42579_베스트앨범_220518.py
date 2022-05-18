from collections import defaultdict

def solution(genres, plays):
    answer = []
    best = defaultdict(list)
    best_g = list()
    i = 0
    for genre, play in zip(genres, plays):
        best[genre].append((play, i))
        i += 1
    for key in list(best.keys()):
        best[key].sort(key = lambda x:x[1])
        best[key].sort(key = lambda x:x[0], reverse=True)
        best_g.append((sum([best[key][i][0] for i in range(len(best[key]))]), key))
    best_g.sort(key = lambda x:x[0], reverse=True)
    for _, key in best_g:
        cnt = 0
        try:
            for k, i in best[key]:
                answer.append(i)
                cnt+=1
                if cnt==2: break
        except:
            continue
                 
    return answer
