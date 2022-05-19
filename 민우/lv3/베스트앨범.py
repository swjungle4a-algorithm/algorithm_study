from collections import defaultdict

def solution(genres, plays):
    album = defaultdict(list)
    answer = []
    
    for genre, play in zip(genres, plays):
        album[genre].append(play)
    
    for i in album.keys():
        album[i].sort(reverse = True) # 장르 내에서 재생 순서 정렬
    
    genre_list = sorted(album.keys(), key = lambda x : sum(album[x]), reverse = True) # 속한 노래가 많이 재생된 장르순으로 정렬
    
    for i in genre_list:
        if len(album[i]) <= 1: # 장르에 속한 곡이 하나일 때
            answer.append(plays.index(album[i][0]))
        
        else: # 장르에 속한 곡이 2개 이상일 때
            a = plays.index(album[i][0])
            b = plays.index(album[i][1])
            
            if album[i][0] == album[i][1]: # 장르 내에서 재생 횟수가 같을 때
                for idx in range(len(plays)):
                    if plays[idx] == album[i][0] and idx != a:
                        b = idx
                        break
                        
                if a < b:
                    answer.append(a)
                    answer.append(b)
                else:
                    answer.append(b)
                    answer.append(a)
                    
            else: 
                answer.append(a)
                answer.append(b)

    return answer
