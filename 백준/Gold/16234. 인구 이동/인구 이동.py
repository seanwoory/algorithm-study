import sys
from collections import deque
def bfs(arr):
    global ans, stop
    v = [[0] * n for _ in range(n)]
    check = 0
    q = deque()
    for i in range(n):
        for j in range(n):
            cnt = 0
            if v[i][j]==0:
                cnt += 1
                change = deque()
                q.append((i, j))
                ppl = 0
                ppl += arr[i][j]
                v[i][j]=1
                change.append((i,j))
                while q:
                    ci,cj = q.popleft()
                    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni,nj = ci+di,cj+dj
                        if 0<=ni<n and 0<=nj<n and v[ni][nj]==0 and l<=abs(arr[ci][cj]-arr[ni][nj])<=r:
                            v[ni][nj]=1
                            ppl += arr[ni][nj] 
                            q.append((ni,nj))
                            change.append((ni,nj))
                            cnt += 1
                            stop = False
                for lst in change:
                    x,y = lst[0],lst[1]
                    arr[x][y] = int(ppl/cnt)
    if not stop:
        ans += 1


n, l, r = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

ans = 0
while True:
    stop = True
    bfs(arr)
    if stop:
        break

print(ans)