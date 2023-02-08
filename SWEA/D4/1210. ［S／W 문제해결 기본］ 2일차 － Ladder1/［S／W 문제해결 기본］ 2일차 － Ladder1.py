N = 10
for tc in range(10):
    n = int(input()) # 버리는수
    arr = [list(map(int, input().split())) for _ in range(100)]
    mi = 99
    for i in range(100):
        if arr[mi][i] == 2:
            mj = i
            break
 
    while mi > 0:
        arr[mi][mj] = 0 
        if mj-1 < 0: 
            if arr[mi][mj+1] == 1:
                mj += 1
            elif arr[mi-1][mj] == 1:
                mi -= 1
            else:
                continue
        elif mj+1>=100: #오른쪽 범위 넘었을 때, 오른쪽 이동 없앰
            if arr[mi][mj-1] == 1:
                mj -= 1
 
            elif arr[mi-1][mj] == 1:
                mi -= 1
            else:
                continue
        else:
            if arr[mi][mj-1] == 1:
                mj -= 1
            elif arr[mi][mj+1] == 1:
                mj += 1
            elif arr[mi-1][mj] == 1:
                mi -= 1
            else:
                continue
    print(f'#{tc+1} {mj}')