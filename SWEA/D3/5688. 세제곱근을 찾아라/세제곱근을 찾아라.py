T=int(input())
for tc in range(1, 1+T):
    N=int(input())
    s,e=1,N
    ans=-1
    while s<=e:
        m=(s+e)//2
        if m**3==N:
            ans=m
            break
        elif m**3<N:
            s=m+1
        elif m**3>N:
            e=m-1

    print(f'#{tc} {ans}')
