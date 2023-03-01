a = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
     (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}
 
 
def change(new):
    ans = []
    idx = len(new)
    num = 0
    n1, n2, n3 = 0, 0, 0
    for i in range(idx):
        if not n1:
            if new[i] == '1':
                num += 1
            elif num:
                n1 = num
                num = 1
        elif not n2:
            if new[i] == '0':
                num += 1
            elif num:
                n2 = num
                num = 1
        elif not n3:
            if new[i] == '1':
                num += 1
            elif num:
                n3 = num
                num = 0
                mn = min(n1, n2, n3)
                ans.append(a[(n1//mn, n2//mn, n3//mn)])
                n1, n2, n3 = 0, 0, 0
    return ans
 
 
def cnt(new):
    ans = change(new)
    idx = 0
    t = 0
    while idx < len(ans):
        if ans[idx:idx+8] not in double:
            double.append(ans[idx:idx+8])
            total = 0
            p = 0
            for i in range(idx, idx + 7, 2):
                total += ans[i] * 3
                p += ans[i]
            for i in range(idx + 1, idx + 7, 2):
                total += ans[i]
                p += ans[i]
            total += ans[idx + 7]
            p += ans[idx+7]
            if not total % 10:
                t += p
        idx += 8
    return t
 
 
ip = int(input().strip())
 
for case in range(1, ip+1):
    double = []
    n, m = map(int, input().strip().split())
    lst = list(set(input().strip() for _ in range(n)))
    lst.sort()
    lst.pop(0)
    code = []
    for line in lst:
        new = ''
        for i in line:
            if i.isdigit():
                d = int(i)
            else:
                d = ord(i) - 55
            dummy = bin(d)[2:]
            new += '0' * (4 - len(dummy)) + dummy
        code.append(new)
    total = 0
    for i in code:
        total += cnt(i)
    print(f'#{case} {total}')
