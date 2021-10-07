def solution(answers):
    answer = []
    
    l = len(answers)
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    person = {1: 0, 2: 0, 3: 0}
    for idx, val in enumerate(answers):
        if person1[idx % 5] == val:
            person[1] += 1
        if person2[idx % 8] == val:
            person[2] += 1
        if person3[idx % 10] == val:
            person[3] += 1

    return [p for p in person if person[p] == max(person.values())]