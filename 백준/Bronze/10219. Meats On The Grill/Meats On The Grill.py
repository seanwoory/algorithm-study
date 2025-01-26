ip = int(input())

for case in range(ip):
    n, m = map(int, input().split())
    for i in range(n):
        a = list(input())
        a.reverse()
        print(''.join(a))