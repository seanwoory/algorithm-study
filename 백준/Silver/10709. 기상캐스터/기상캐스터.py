# 남북방향 H, 동서방향 W
# 북쪽으로부터 i번째, 서쪽으로부터 j번째 => (i,j)
# 1분 지날 때마다 1키로 동쪽씩

H,W=map(int,input().split())
arr=[input() for _ in range(H)]
ans=[[-1]*W for _ in range(H)]

for i in range(H):
    flag=False
    for j in range(W):
        if arr[i][j]=='c':
            n=0
            ans[i][j]=n
            flag=True
        elif flag:
            n+=1
            ans[i][j] = n
        elif arr[i][j]=='.':
            flag=False
            n=0
            continue
for lst in ans:
    print(*lst)