def solution(lottos, win_nums):
    
    rank = [6, 6, 5, 4, 3, 2, 1]  # rank[일치하는 번호 개수] = 순위
    win_cnt = 0      #일치하는 번호 개수 
    zero_cnt = 0     #알아볼 수 없는 번호 개수
        
    for num in lottos:
        if num in win_nums:
            win_cnt += 1
        elif num == 0:
            zero_cnt += 1
            
    answer = [rank[win_cnt + zero_cnt], rank[win_cnt]]
        
    return answer
