T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    cnt = [0] * 5001
    idx = []
    ans = []
 
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            cnt[j] += 1
 
    p = int(input())
    for i in range(p):
        idx.append(int(input()))
 
    for index in idx:
        ans.append(cnt[index])
 
    b = ' '.join(map(str, ans))
    print(f'#{test_case} {b}')