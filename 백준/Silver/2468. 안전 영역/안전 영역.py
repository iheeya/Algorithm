import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)  # 맨 위에 추가

def dfs(x, y, w):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if A[nx][ny] > w and not visited[nx][ny]:
                dfs(nx, ny, w)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
result = 0
max_height = max(map(max, A))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for water in range(0, max_height + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j] > water and not visited[i][j]:
                cnt +=1
                dfs(i, j, water) 

    result = max(result, cnt)


print(result)