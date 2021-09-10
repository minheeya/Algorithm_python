def solution(dartResult):

    digits = ''
    ops = ''
    for char in dartResult:
        if char.isdigit():
            digits += char
        else:
            ops += char
            digits += ' '
    
    scores = [int(i) for i in digits.split(' ') if i != '']
    
    i = 0
    sdt_dic = {'S': 1, 'D': 2, 'T': 3}
    for op in ops:
        if op in 'SDT':
            scores[i] **= sdt_dic[op]
            i += 1
        elif op == '*':
            scores[i - 1] *= 2
            if i - 2 >= 0:
                scores[i - 2] *= 2
        else:
            scores[i - 1] *= -1

    return sum(scores)