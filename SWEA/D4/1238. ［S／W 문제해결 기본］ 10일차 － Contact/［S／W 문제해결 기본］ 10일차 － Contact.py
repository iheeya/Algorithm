# bfs의 depth와 마지막 레벨을 이용해 마지막으로 방문한 가장 큰 수를 찾아라
def bfs(start):
    q = [start]
    visited = [0] * 101  # 연락 최대인원의 수만큼 방문체크할 배열 만들기
    visited[start] = 1

    max_level = 1   # 현재 깊이를 저장할 변수
    max_number = start   # 현재 깊이에서 가장 큰 수를 저장할 변수

    while q:   # q가 모두 빌때까지 반복
        now = q.pop(0)    # now: 현재 노드의 값

        for to in graph[now]:   # 현재 노드 now에서 갈 수 있는 다음 노드 to
            # 이미 방문한 노드라면 pass
            if visited[to]:
                continue

            # 현재 level 계산 : 이전 level(now의 레벨) + 1
            # level을 visited 배열에 저장
            visited[to] = visited[now] + 1

            # 현재 max_level에 저장된 수가 현재 깊이보다 작다면 깊이, max_number 갱신
            # 깊이는 같지만 노드의 수가 이전 보다 크다면 max_number 갱신
            if max_level < visited[to] or (max_level == visited[to] and max_number < to):
                max_level = visited[to]
                max_number = to

            q.append(to)   # q에 새로 방문하는 노드들 저장

    return max_number


for test_case in range(1, 11):
    N, start = map(int, input().split()) # N: 데이터의 길이, start: 시작점
    g = list(map(int, input().split()))  # 그래프 데이터 입력받기
    graph = [[] for _ in range(101)]    # 연락 최대인원의 수만큼 그래프 만들기

    # 그래프 : 방향이 있는 그래프
    for i in range(0, N, 2):
        # 하나의 노드에서 여러 노드로 갈 수 있으므로 =으로 할당하는 것이 아니라 append
        graph[g[i]].append(g[i+1])   # 시작 노드 점에 도착 노드 append


    result = bfs(start)
    print(f'#{test_case} {result}')