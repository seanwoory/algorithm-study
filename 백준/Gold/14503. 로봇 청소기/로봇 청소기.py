import sys

n, m = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
v = [[0]*m for _ in range(n)]
ans = 0

ci, cj = si, sj
if arr[ci][cj]==0:
    ans += 1
    v[ci][cj]=1
while True:
    flag = True
    for _ in range(4):
        dr = (dr+3)%4
        ni,nj = ci+di[dr], cj+dj[dr]
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0 and v[ni][nj]==0:
            ans += 1
            v[ni][nj]=1
            ci,cj = ni,nj
            flag=False
            break
    if flag:
        dr = (dr+2)%4
        ni,nj = ci+di[dr], cj+dj[dr]
        if arr[ni][nj]==1:
            break
        else:
            ci,cj = ni,nj
            dr = (dr-2)%4

print(ans)