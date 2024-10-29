n,k = map(int,input().split())
lst = list(map(str,input()))
v = [0] * n
cnt = 0

for i in range(n):
    if lst[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0<= j <n and lst[j] == 'H' and v[j] == 0:
                v[j] = 1
                cnt += 1
                break

print(cnt)
