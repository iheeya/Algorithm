from collections import deque

def bfs():
    q = deque()
    q.append([start_x, start_y])

    while q:
        x, y = q.popleft()

        # 50m에 한병씩 맥주를 마셔야 한다.
        # 두 좌표사이의 거리는 (x좌표의 차 + y 좌표의차)
        if abs(x- penta_x) + abs(y - penta_y) <= 1000:
            print('happy')
            return 

        for i in range(n):
            if not visited[i]:
                nx, ny = graph[i]
                if abs(x-nx) + abs(y-ny) <=1000:
                    q.append([nx, ny])
                    visited[i] = 1

    print('sad')
    return 



T = int(input())

for test_case in range(T):
    n = int(input())   # 편의점의 개수
    store = [0] * (n+1)
    graph = []
    visited = [0 for _ in range(n+1)]   # 스타트 좌표 제와하고 만들기

    start_x, start_y = map(int, input().split()) # 스타트 좌표
    for i in range(n):    # 편의점 좌표
        x, y = map(int, input().split())
        graph.append([x, y])
    
    penta_x, penta_y = map(int, input().split())   # 도착 좌표

    # # 출력: 갈수 있으면 'happy', 없으면 'sad'
    bfs()