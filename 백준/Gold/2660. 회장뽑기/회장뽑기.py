from collections import deque

N = int(input())
members = [[] for _ in range(N+1)]

while True:
    s, e = map(int, input().split())
    if s == e == -1:
        break
    members[s].append(e)
    members[e].append(s)
    
relations = [[51 for _ in range(N)] for _ in range(N+1)]
scores = []

for start in range(1, N+1):
    queue = deque([[start, 0]])

    while queue:
        mem, score = queue.popleft()
        relations[start][mem-1] = min(relations[start][mem-1], score)
        
        mem_friends = members[mem]		
        for mf in mem_friends:
            if relations[start][mf-1] == 51:
                queue.append([mf, score+1])

for i in range(1, N+1):
    scores.append(max(relations[i]))

minimum = min(scores)
candidates = [i+1 for i in range(N) if scores[i] == minimum]

print(f'{minimum} {len(candidates)}')
print(*candidates)