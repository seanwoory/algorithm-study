# 가장 큰 반 아이에게 가장 큰 번호 부여
P=int(input())
for tc in range(1,P+1):
    # 키를 줄서기 차례의 순서대로 밀리미터 단위로 나타낸 것.
    lst=list(map(int, input().split()))
    lst.pop(0)
    ans=0
    comp=sorted(lst)
    data=[lst.pop(0)]
    while lst:
        # 기준으로 비교할 원소
        data.append(lst.pop(0))
        for i in range(1,len(data)):
            for j in range(i):
                if data[j]>data[i]:
                    data.insert(j, data.pop(i))
                    ans+=len(data)-(j+1)
        if comp==data:
            break
        
    print(f'{tc} {ans}')