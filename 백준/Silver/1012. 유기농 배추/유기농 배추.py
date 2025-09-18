import sys
from collections import deque
input = sys.stdin.readline

T = int(input())   # 테스트 케이스 수

for _ in range(T):
    M, N, K = map(int, input().split())   # 가로, 세로, 배추 개수
    A = [[0] * M for _ in range(N)]       # 세로 N, 가로 M
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        A[y][x] = 1                       # (y, x) 좌표에 배추 심기

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sy][sx] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[ny][nx] and A[ny][nx] == 1:
                        visited[ny][nx] = True
                        q.append((nx, ny))

    cnt = 0
    for y in range(N):
        for x in range(M):
            if A[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                cnt += 1

    print(cnt)
