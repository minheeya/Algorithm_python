def solution(progresses, speeds):
    
    Q = []
    for progress, speed in zip(progresses, speeds):
        if not Q or Q[-1][0] < -((progress - 100) // speed):
            Q.append([-((progress - 100) // speed), 1])
        else:
            Q[-1][1] += 1
            
    return [q[1] for q in Q]