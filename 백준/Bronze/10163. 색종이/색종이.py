n = int(input())
ans = [[0 for _ in range(1001)] for _ in range(1001)]
dct = dict()
for i in range(1, n+1):
    dct[i] = 0
    dummy = list(map(int, input().split()))
    for j in range(dummy[0], dummy[0] + dummy[2]):
        for k in range(dummy[1], dummy[1] + dummy[3]):
            if ans[j][k]:
                dct[ans[j][k]] -= 1
                dct[i] += 1
                ans[j][k] = i

            else:
                dct[i] += 1
                ans[j][k] = i


for i in range(1, n+1):
    print(dct[i])