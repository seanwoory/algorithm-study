def palLong(arr):
    lst = []
    for l in range(100)[::-1]: # 문자열 길이, 제한시간 초과로 인해 긴 문자열부터 차례로 거르자.
        for j in range(100): # 확인할 대상 리스트 인덱스
            for i in range(0, 100-l+1): # 가로 처음 시작 인덱스
                if arr[j][i:i+l] == arr[j][i:i+l][::-1]:
                    lst.append(l)
                    break
    return lst[0]

T = 10
for tc in range(1, 1+T):
    _ = input()
    garr = [list(map(str, input())) for _ in range(100)]
    sarr = list(map(list,zip(*garr)))
    ans = [palLong(garr), palLong(sarr)]

    print(f'#{tc} {max(ans)}')
