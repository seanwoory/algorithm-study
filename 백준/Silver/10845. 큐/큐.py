import sys
input = sys.stdin.readline
n = int(input())

que = []
for i in range(n):
    lst = input().split()

    if lst[0] == 'push':
        que.append(lst[1])

    if lst[0] == 'pop':
        if len(que) != 0:
            print(que.pop(0))
        else:
            print(-1)
    if lst[0] == 'size':
        print(len(que))
    if lst[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if lst[0] == 'front':
        if len(que) != 0 :
            print(que[0])
        else:
            print(-1)
    if lst[0] == 'back':
        if len(que) != 0:
            print(que[-1])
        else:
            print(-1)