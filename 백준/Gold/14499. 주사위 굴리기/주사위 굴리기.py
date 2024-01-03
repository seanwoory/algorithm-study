N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

n1=n2=n3=n4=n5=n6=0
di, dj = [0,0,0,-1,1], [0,1,-1,0,0]
alst = []

for dr in lst:
    ni, nj = ci+di[dr], cj+dj[dr]
    if 0<=ni<N and 0<=nj<M:
        if dr==1:
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif dr==2:
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif dr==3:
            n1,n2,n5,n6 = n5,n1,n6,n2
        else:
            n1,n2,n5,n6 = n2,n6,n1,n5


        if arr[ni][nj]==0:
            arr[ni][nj]=n6
        else:
            n6, arr[ni][nj]=arr[ni][nj],0
        
        alst.append(n1)
        ci, cj = ni, nj
        
print(*alst, sep='\n')