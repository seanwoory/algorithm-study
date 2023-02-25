N=int(input())
cnt=ans=0

while N>=0:
    if N%5==0:
        ans += N // 5
        break
    else:
        N -= 3
        ans += 1
else:
    ans=-1
print(ans)