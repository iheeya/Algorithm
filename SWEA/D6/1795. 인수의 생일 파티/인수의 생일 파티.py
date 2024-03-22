from heapq import heappop, heappush

def dijkstra(start, end):
    pq = []
    visited = [1e9] * (N + 1)

    heappush(pq, (0, start))   # pq에 가중치와 시작값 저장
    visited[start] = 0      # 방문 체크
    result = 0   # 결과를 저장할 리스트

    while pq:
        dist, now = heappop(pq)

        for to in graph[now]:
            next_dist = to[0]    # 다음 거리
            next_node = to[1]    # 다음 노드

            new_dist = next_dist + dist   # 다음 노드 까지의 가중치 저장

            # 새로운 거리보다 이미 있는 거리가 작거나 같다면
            if new_dist >= visited[next_node]:
                continue

            # 다음 노드에 가는 가중치 저장
            visited[next_node] = new_dist

            if next_node == end:
                result = visited[next_node]
                break

            heappush(pq, (new_dist, next_node))

    return result




T = int(input())

for test_case in range(1, T+1):
    # N: 집의 개수, M: 간선의 개수, X: 인수의 집 번호
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    result = 0    # 가장 오래 걸리는 시간을 저장할 변수

    # 그래프 만들기
    for _ in range(M):
        s, e, w = map(int, input().split())   # 시작점, 도착점, 가중치
        graph[s].append([w, e])   # 현재 노드 위치에 가중치와 연결된 노드 저장

    for i in range(1, N+1):
        if i == X:
            continue

        go = dijkstra(i, X)
        back = dijkstra(X, i)
        time = go + back

        if time > result:
            result = time


    # 출력: 인수의 집으로 오고 가는 시간이 가장 오래 걸리는 집의 시간
    print(f'#{test_case} {result}')