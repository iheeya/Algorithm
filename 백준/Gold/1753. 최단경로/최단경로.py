import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())    # 시작 정점
A = [[] for _ in range(V+1)]    # 인접 리스트
D = [sys.maxsize] * (V + 1)    # 최단 거리 리스트
D[start] = 0    # 시작노드의 가중치 설정
visited = [False] * (V+1)   # 방문여부 체크를 위한 리스트

for _ in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))     # 인접 리스트에 연결노드와 가중치 같이 저장

heap = []
heapq.heappush(heap, (D[start], start))   # 가중치, 시작 정점 우선순위 큐에 넣기

while heap:
    dist, tmp = heapq.heappop(heap)
    # 이미 방문한 노드면 스킵
    if visited[tmp]:
        continue
    # 현재 노드 방문 상태로 변경
    visited[tmp] = True

    for nxt, weight in A[tmp]:
        if D[nxt] > D[tmp] + weight:
            D[nxt] = D[tmp] + weight
            heapq.heappush(heap, (D[nxt], nxt))


for i in range(1, V+1):
    if visited[i]:
        print(D[i])
    else:
        print('INF')
