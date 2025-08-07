import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())   # 도시개수, 도로개수, k번째 최단경로
A = [[] for _ in range(n+1)]   # 인접리스트
D = [[sys.maxsize] * k for _ in range(n+1)]     # 거리리스트
D[1][0] = 0    # 스타트 노드는 1번 노드

for _ in range(m):
    a, b, c = map(int, input().split())   # a, b: 노드  c: 걸리는 시간(가중치)
    A[a].append((b, c))   # 다음 노드, 다음 노드까지 가는데 걸리는 시간 순으로 입력

hq = [(0, 1)]    # 힙큐 선언 (우선순위 노드를 저장할 큐) / (가중치, 노드 번호)

while hq:
    w, node = heapq.heappop(hq)

    for nNode, nCost in A[node]:
        result = nCost + w
        if D[nNode][k-1] > result:
            D[nNode][k-1] = result
            D[nNode].sort()
            heapq.heappush(hq, [result, nNode])


for i in range(1, n+1):
    if D[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(D[i][k-1])


