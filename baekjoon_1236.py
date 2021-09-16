N, M = map(int, input().split())

castle = [input() for _ in range(N)]

n_need = 0
for s in castle:
    if 'X' not in s:
        n_need += 1
        
m_need = 0
for s in list(zip(*castle)):
    if 'X' not in s:
        m_need += 1

print(max(n_need, m_need))