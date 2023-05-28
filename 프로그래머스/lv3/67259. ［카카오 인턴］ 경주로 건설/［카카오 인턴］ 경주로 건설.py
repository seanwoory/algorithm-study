from collections import deque
def solution(board):
    n = len(board)
    directions = ((-1,0),(1,0),(0,-1),(0,1))

    def bfs(x,y,cost,d):
        v = [[0]*n for _ in range(n)]
        q = deque()
        q.append((x,y,cost,d))

        while q:
            x, y, cost, dr = q.popleft()
            for i in range(4):
                ni, nj = x + directions[i][0], y + directions[i][1]

                if 0<=ni<n and 0<=nj<n and board[ni][nj]==0:
                    if dr==i:
                        newcost = cost + 100
                    else:
                        newcost = cost + 600

                    if v[ni][nj]==0 or  v[ni][nj]>newcost:
                        q.append((ni,nj,newcost,i))
                        v[ni][nj] = newcost
        return v[n-1][n-1]
    return min(bfs(0,0,0,1), bfs(0,0,0,3))