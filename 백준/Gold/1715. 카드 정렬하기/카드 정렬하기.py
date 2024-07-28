from sys import stdin
import heapq

n = int(stdin.readline())
heap = []
for i in range(n):
    a = int(stdin.readline())
    heapq.heappush(heap, a)

ans = 0
for i in range(n-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a+b
    heapq.heappush(heap, a+b)

print(ans)