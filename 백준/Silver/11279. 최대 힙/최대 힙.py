import heapq, sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    num = int(input())

    if num != 0:
        heapq.heappush(lst, -num)
    else:
        if lst:
            print(-heapq.heappop(lst))

        else:
            print(0)