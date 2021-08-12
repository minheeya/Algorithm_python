#장르별 가장 많이 재생된 노래를 2개씩 모아 베스트앨범 만듬
#총 재생횟수가 가장 많은 장르부터 수락함(가장 횟수가 많은 곡 부터, 횟수 같으면 고유번호 작은것 부터 수락)
from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    #genre_dict = {장르: [(재생횟수, 노래고유번호),..] }
    genre_dict = defaultdict(list)   
    for i, genre, play_n in zip(range(len(genres)), genres, plays):
        genre_dict[genre].append((play_n, i))
        
    #genre_sort = 총 재생횟수가 가장 높은순으로 장르가 담겨있는 list
    genre_sort = sorted(list(genre_dict.keys()), key = lambda x: -sum(map(lambda y: y[0], genre_dict[x])))
    
    for genre in genre_sort:
        #genre_dict의 값들을 가장 많이 재생된순으로 정렬 후, 노래번호가 가장 적은순으로 정렬
        genre_dict[genre].sort(key = lambda x: (-x[0], x[1]))
        #장르별로 노래 2개를 앨범에 추가
        answer.extend([song_n for play_n, song_n in genre_dict[genre][:2]])
    
    return answer