import sys
from itertools import combinations

def distance(i,j):
    lst = []
    for ni,nj in chick_lst:
        lst.append(abs(i-ni)+abs(j-nj))
    return lst

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chick_lst = []
chick_num = 0

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chick_lst.append((i,j))
            chick_num += 1
                
total = []
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            total.append(distance(i,j))

numb = list(range(chick_num))

ans = 2500
for pick in combinations(numb,m):
    tmp_a = 0
    for lst in total:
        tmp = []
        for i in pick:
            tmp.append(lst[i])
        tmp_a += min(tmp)
    if ans > tmp_a:
        ans = tmp_a
        
print(ans)