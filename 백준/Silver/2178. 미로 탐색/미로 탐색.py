import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == 1:
            A[nx][ny] += A[x][y]   # 거리계산
            q.append((nx, ny))

print(A[N-1][M-1])