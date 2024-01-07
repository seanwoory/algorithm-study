import sys
input = sys.stdin.readline

n = int(input())
deque = []

for i in range(n):
    lst = input().split()

    if lst[0] == 'push_back':
        deque.append(lst[1])
    if lst[0] == 'push_front':
        deque.insert(0, lst[1])
    if lst[0] == 'pop_back':
        if len(deque) != 0:
             print(deque.pop(-1))
        else:
             print(-1)
    if lst[0] == 'pop_front':
        if len(deque) != 0:
             print(deque.pop(0))
        else:
             print(-1)
    if lst[0] == 'size':
        print(len(deque))
    if lst[0] == 'empty':
        if len(deque) == 0 :
             print(1)
        else:
             print(0)
    if lst[0] == 'back':
        if len(deque) != 0 :
             print(deque[-1])
        else:
             print(-1)
    if lst[0] == 'front':
        if len(deque) != 0 :
             print(deque[0])
        else:
             print(-1) 