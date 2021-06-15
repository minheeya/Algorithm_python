def solution(enroll, referral, seller, amount):
    answer = dict()   #이름 : 분배 후 이익 (초기값은 0)
    group = dict()    #이름 : 참여시킨 다른 사람 이름
    
    for i in range(len(enroll)):
        answer[enroll[i]] = 0
        group[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        name = seller[i]
        income = amount[i]*100  #분배 전 수익
        while name != '-':
            if income // 10 < 1:
                answer[name] += income
                break
            else:
                answer[name] += income - (income // 10) 
                name = group[name]  #윗 사람 
                income //= 10   #윗 사람이 받는 이득
                
    return list(answer.values())