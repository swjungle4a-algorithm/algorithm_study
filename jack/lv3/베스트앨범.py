def solution(genres, plays):
    sumOfGenre = {x : 0 for x in genres}
    cntOfPlay = {x : [] for x in genres}
    answer = []
    
    for i in range(len(genres)) :
        sumOfGenre[genres[i]] += plays[i]
        cntOfPlay[genres[i]].append((plays[i],i))

    for genre, val in sorted(sumOfGenre.items(), key=lambda x: x[1], reverse=True) :
        if len(cntOfPlay[genre]) > 1 :
            cntOfPlay[genre].sort(key = lambda x : x[1])
            cntOfPlay[genre].sort(key = lambda x : x[0], reverse=True)
            answer.extend(map(lambda x: x[1], cntOfPlay[genre][:2]))
        else :
            answer.append(cntOfPlay[genre][0][1])
    return answer
