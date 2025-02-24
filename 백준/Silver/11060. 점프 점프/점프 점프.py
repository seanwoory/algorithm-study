from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    visit[0] = 1
    while q:
        v = q.popleft()
        for i in range(1, lst[v[0]]+1):
            if v[0]+i < n and not visit[v[0]+i]:
                q.append([v[0]+i, v[1]+1])
                visit[v[0]+i] = 1
                if v[0]+i == n-1:
                    return v[1]+1
    return -1


n = int(input())
if n == 1:
    print(0)

else:
    lst = list(map(int, input().split()))
    visit = [0 for _ in range(n)]
    print(bfs())