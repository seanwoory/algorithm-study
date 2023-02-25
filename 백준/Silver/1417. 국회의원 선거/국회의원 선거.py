N=int(input())
# 누구를 찍을 지 알 수 있음
# 후보 N명, 주민 M명
# 다른 모든 사람의 득표수보다 많은 득표수를 가질 때 그 사람이 국회의원 당선
# 다솜이는 기호 1번

lst=[int(input()) for _ in range(N)]
cnt=0
while True:
    if N<=1:
        break
    if lst[0]<=max(lst[1:]):
        for i in range(1,N):
            if lst[i]==max(lst[1:]):
                lst[i]-=1
                break
        lst[0]+=1
        cnt+=1
    else:
        break
print(cnt)