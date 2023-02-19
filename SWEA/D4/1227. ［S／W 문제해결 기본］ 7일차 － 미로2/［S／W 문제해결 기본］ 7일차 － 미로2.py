def dfs(si,sj):
    ci,cj=si,sj
    stk=[]
    while True:
        for di,dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni,nj=ci+di,cj+dj
            if 0<=ni<100 and 0<=nj<100 and arr[ni][nj]!='1':
                stk.append([ci,cj])
                ci,cj=ni,nj
                arr[ci][cj]='1'
                break
        else:
            if stk:
                ci,cj=stk.pop()
            else:
                break


T=10
for tc in range(1, 1+T):
    _=input()
    arr=[list(input()) for _ in range(100)]
    arr=arr[::-1]
    ans='1'
    for i in range(100):
        for j in range(100):
            if arr[i][j]=='2':
                si,sj=i,j
            elif arr[i][j]=='3':
                ei,ej=i,j

    dfs(si,sj)
    if arr[ei][ej]!='1':
        ans='0'
    print(f'#{tc} {ans}')