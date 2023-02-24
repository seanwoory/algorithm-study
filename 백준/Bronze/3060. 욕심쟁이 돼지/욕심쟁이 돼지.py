T=int(input())
for _ in range(T):
    N=int(input())
    lst=list(map(int, input().split()))
    ans = 0
    if sum(lst)<=N:
        ans+=1


    # 첫날에는 lst 원소 전부 다 합
    # 둘째날부터는? idx, idx-1, idx+1, (idx+3)%6 더해서 sum
    # 첫째 둘째 돌때마다, sm이 N을 넘으면 break
    while True:
        temp=lst[:]
        for i in range(len(lst)):
            lst[i]=temp[i]+temp[i-1]+temp[(i+1)%6]+temp[(i+3)%6]
        sm=sum(lst)
        if sm>N:
            ans+=1
            break
        else:
            ans+=1
    print(ans)