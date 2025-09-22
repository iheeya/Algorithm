import sys
input = sys.stdin.readline

T = int(input())

def dfs(x):
    visited[x] = True
    nx = p[x]
    if not visited[nx]:
        dfs(nx)

for tc in range(T):
    N = int(input())
    p = [0] +  list(map(int, input().split()))   # 단방향 순열
    visited = [False] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
