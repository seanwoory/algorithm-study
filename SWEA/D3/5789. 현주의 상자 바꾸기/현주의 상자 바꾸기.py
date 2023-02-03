T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    lst = []
    for i in range(q):
        lst.append(list(map(int, input().split())))
    box = [0] * n
    i = 0
    for a in lst:
        i += 1
        box[a[0]-1 : a[1]] = list(i for _ in range(a[1]-a[0]+1))


    print(f'#{test_case}', *box)