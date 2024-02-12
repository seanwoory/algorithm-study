S = input()
n = int(input())
ans = ''
for i in range(len(S)):
    if (n-1) == i:
        ans = S[i]

print(ans) 