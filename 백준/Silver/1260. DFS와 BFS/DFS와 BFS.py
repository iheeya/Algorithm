import sys
input = sys.stdin.readline
from collections import deque

def DFS(V):
    print(V, end = " ")
    visited_dfs[V] = True
    for i in A[V]:
        if not visited_dfs[i]:
            DFS(i)

def BFS(V):
    q = deque()
    q.append(V)

    while q:
        n = q.popleft()
        print(n, end = " ")
        visited_bfs[n] = True
        for i in A[n]:
            if not visited_bfs[i] :
                q.append(i)
                visited_bfs[i] = True



N, M, V = map(int, input().split())    # 정점 개수, 간선 개수, 탐색을 시작할 정점 번호
A = [[] for _ in range(N+1)] 

for _ in range(M):
    i, j = map(int, input().split())
    A[i].append(j)
    A[j].append(i)

# 정점이 여러개 연결되어 있는 경우 작은 수 먼저 방문하도록
for i in range(N+1):
    A[i].sort()

# 인덱스 번호 == 노드 번호
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


DFS(V)
print()
BFS(V)



