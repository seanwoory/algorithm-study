st = input()
ans=cnt=0
for i in range(len(st)):
    if st[i]=='(':
        cnt+=1
    else: # ')' 바로 앞의 기호를 확인해야함.
        if st[i-1]=='(': # 레이저의 경우,
            cnt-=1
            ans+=cnt
        else:
            cnt-=1
            ans+=1
print(ans)