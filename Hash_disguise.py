from collections import Counter
from functools import reduce

def solution(clothes):
    
    clothes_dic = Counter([part for cl, part in clothes])
    answer = reduce(lambda acc,cur: acc*(cur + 1), clothes_dic.values(), 1) - 1
    
    return answer