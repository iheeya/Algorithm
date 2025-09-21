import sys
input = sys.stdin.readline

def dfs(x, y):
    global h_num
    h_num += 1
    A[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if A[nx][ny] == 1:
                dfs(nx, ny)


N = int(input())
A = [list(map(int, input().strip())) for _ in range(N)]

cnt = 0    # 단지 수를 저장할 변수
result = []   # 단지내 집의 수를 저장할 변수

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(N):
        h_num = 0
        if A[i][j] == 1:
            cnt += 1
            dfs(i, j)
            result.append(h_num)

print(cnt)
result.sort()
for i in range(len(result)):
    print(result[i])