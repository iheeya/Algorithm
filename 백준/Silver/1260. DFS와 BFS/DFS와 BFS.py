from collections import deque

def bfs(bfs_lst):
    global bq, visited_bfs

    while bq:
        node = bq.popleft()
        if  not visited_bfs[node]:
            visited_bfs[node] = True
            bfs_lst.append(node)
        
        graph[node].sort()  # 정점이 여러개인 경우 더 작은것 부터 방문
        for next in graph[node]:
            if not visited_bfs[next]:
                bq.append(next)
    
    return bfs_lst


def dfs(start, dfs_lst):
    global dq, visited_dfs

    # 가지치기: 이미 방문한 노드라면 종료
    if visited_dfs[start]:
        return

    dq.append(start)
    while dq:
        node  = dq.popleft()
        if not visited_dfs[node]:
            visited_dfs[node] = True
            dfs_lst.append(node)
        
        graph[node].sort()
        for next in graph[node]:
            dfs(next, dfs_lst)
    
    return dfs_lst




N, M, V = map(int, input().split())
# N: 정점의 개수  M: 간선의 개수  V: 탐색을 시작할 정점의 번호

visited_bfs = [False] * (N+1)   # 방문체크를 위한 배열
visited_dfs = [False] * (N+1)   # 방문체크를 위한 배열
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())   # 서로 연결된 정점들
    graph[a].append(b)
    graph[b].append(a)

bq = deque()  # bfs에서 사용할 deque
bq.append(V)

bfs_result = bfs([])

dq = deque()   # dfs에서 사용할 deque
dfs_result = dfs(V, [])

# 출력: 첫째 줄 DFS 실행 결과, 둘째 줄 BFS 실행 결과
print(*dfs_result)
print(*bfs_result)