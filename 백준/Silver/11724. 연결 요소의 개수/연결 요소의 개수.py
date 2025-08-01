import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(n):
    visited[n] = True    # 해당 노드 방문 처리
    
    for i in A[n]:    # 인접 리스트 순회
        if visited[i] == False:    # 해당 노드가 미방문 상태라면
            DFS(i)    # DFS를 통해 방문할 수 있도록

    
N, V = map(int, input().split())    # 노드, 간선의 개수
A = [[] for _ in range(N+1)]    # 인접 리스트
count = 0    # 연결 요소의 개수 저장
visited = [False] * (N + 1)    # 방문 여부를 저장할 리스트

for _ in range(V):
    u, v = map(int, input().split())   # 간선의 양 끝 점
    A[u].append(v)     # 인접 리스트에 연결된 점 저장
    A[v].append(u)

for i in range(1, N+1):
    if visited[i] == False:    # 아직 방문하지 않은 노드라면
        count += 1      # 연결 요소의 시작이므로 카운트
        DFS(i)          # 인접 리스트를 탐색하기 위한 DFS 함수 실행


print(count)