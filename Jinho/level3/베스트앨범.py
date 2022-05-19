from collections import defaultdict

def solution(genres, plays):
    
    answer = []
    genres_count = {}
    
    for genre in set(genres):
        genres_count[genre] = 0
    
    plays_index = defaultdict(list)

    for i, genre in enumerate(genres):
        genres_count[genre] += plays[i]
        plays_index[genre].append([i, plays[i]])
    print(genres_count)
    genres_count = sorted(genres_count.items(), key = lambda item: item[1], reverse = True)

    for genre, _ in genres_count:
        song_list = plays_index[genre]
        if len(song_list) == 1:
            answer.append(song_list[0][0])
        else:
            song_list_sorted = sorted(song_list, key=lambda x:x[0])
            song_list_sorted = sorted(song_list, key=lambda x:x[1], reverse=True)
            answer.append(song_list_sorted[0][0])
            answer.append(song_list_sorted[1][0])
                
    return answer
