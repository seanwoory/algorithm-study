import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

maxx = 0
sec = sys.maxsize  # 정수 최댓값 할당.

for floor in range(257):
    over, lack = 0, 0
    for k in range(n):
        for j in range(m):
            if arr[k][j] > floor:  # 초과분
                over += (arr[k][j] - floor)
            else:
                lack += (floor - arr[k][j])  # 부족분

    if over + b >= lack: # 초과가 부족보다 많으면 (평평하게 할 수 있음)
        if (over*2) + lack <= sec:
            sec = (over * 2) + lack
            maxx = floor  # 가장 높은 층


print(sec, maxx) 