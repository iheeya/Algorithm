from heapq import heappush, heappop

def dijkstra(start):
    pq = []  # 방문 노드를 저장할 리스트
    visited[start] = 0    # 시작 노드의 거리: 0
    heappush(pq, (0, start))  # 현재 가중치와 시작점 저장

    while pq:
        dist, now = heappop(pq)  # 우선순위 큐에 있는 값 pop

        for to in graph[now]:   # 현재 노드에서 갈 수 있는 가중치와 노드 == to
            next_dist = to[0]
            next_node = to[1]

            new_dist = dist + next_dist

            # 새로운 거리보다 이미 있는 거리가 작거나 같다면
            if new_dist >= visited[next_node]:
                    continue

            visited[next_node] =  new_dist   # 다음노드의 누적 거리 = new_dist
            heappush(pq, (new_dist, next_node))   # 다음 노드의 가중치와 노드 저장




T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())   # 노드의 개수, 간선의 개수
    graph = [[] for _ in range(V+1)]   # 그래프 만들기
    visited = [1e9] * (V+1)     # 인덱스 == 노드 번호, 노드들의 누적 거리를 저장할 리스트

    for _ in range(E):
        s , e, w = map(int, input().split())   # 시작점, 끝점, 가중치 저장
        graph[s].append([w, e])    # 시작점에 가중치, 도착점 저장


    dijkstra(0)
    result = visited[-1]
    print(f'#{test_case} {result}')