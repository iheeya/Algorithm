import sys
from collections import deque
input = sys.stdin.readline

N, V, I = map(int, input().split())    # 노드, 간선, 시작 노드
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
A = [[] for _ in range(N+1)]   # 인접 리스트

# 인접 리스트 만들기
for i in range(V):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)


# 인접 리스트 오름차순으로 정렬
for i in range(N+1):
    A[i].sort()

def DFS(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    for i in A[v]:
        if not visited_dfs[i]:
            DFS(i)

def BFS(v):
    deq = deque()

    deq.append(v)

    while deq:
        node_now = deq.popleft()
        visited_bfs[node_now] = True

        for i in A[node_now]:
            if not visited_bfs[i]:
                deq.append(i)
                visited_bfs[i] = True
        
        print(node_now, end = ' ')


DFS(I)
print()   # 줄 바꿈을 위한 코드
BFS(I)