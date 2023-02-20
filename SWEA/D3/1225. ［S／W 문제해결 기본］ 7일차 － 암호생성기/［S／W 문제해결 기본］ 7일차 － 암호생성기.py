T = 10
for tc in range(1, 1+T):
    _ = int(input())
    lst=list(map(int, input().split()))

    pr=0
    flag=True
    while flag:
        for i in range(len(lst)):
            pr=pr%5+1
            lst.append(lst.pop(0)-pr)
            if lst[-1]<=0:
                lst[-1]=0
                flag=False
                break
    print(f'#{tc}', *lst)