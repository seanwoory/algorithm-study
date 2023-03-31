dr = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(n,ci,cj,sm):
    global ans

    if n==3:
        ans=max(ans, sm)
        return

    for di,dj in dr:
        ni,nj = ci+di,cj+dj
        if 0<=ni<N and 0<=nj<M and (ni,nj) not in v:
            v.append((ni,nj))
            dfs(n+1,ni,nj,sm+arr[ni][nj])
            v.pop()
            v.append((ni, nj))
            dfs(n+1,ci,cj,sm+arr[ni][nj])
            v.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans=0

for ci in range(N):
    for cj in range(M):
        v = [(ci,cj)]
        dfs(0,ci,cj,arr[ci][cj])

print(ans)