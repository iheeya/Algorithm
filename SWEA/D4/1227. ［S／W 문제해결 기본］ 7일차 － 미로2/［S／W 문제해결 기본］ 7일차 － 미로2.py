from collections import deque

def bfs(a, b):
    global q

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q.append([a, b])  # 시작점 enqueue
    visited[a][b] = 1  # 시작점 방문표시

    while q:  # q가 모두 빌때까지
        cx, cy = q.popleft()

        for k in range(4):
            nx = dx[k] + cx
            ny = dy[k] + cy
            if 0 <= nx < 100 and 0 <= ny < 100:  # 현재 좌표가 미로의 범위 안에 있다면
                if maze[nx][ny] == 0 and visited[nx][ny] == 0:  # 현재 위치가 통로이고 아직 방문하지 않았다면
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif maze[nx][ny] == 3:    
                    return 1    # 도착지점에 도착했다면 1 반환

    return 0    # 도착지점에 도착하지 못했다면 0 반환



for test_case in range(1, 11):
    tc = int(input())   # 테스트케이스 넘버
    maze = [list(map(int, input())) for _ in range(100)]    # 100 X 100 크기의 미로 생성
    # 1: 벽, 0: 통로 2: 출발, 3: 도착
    q = deque()

    visited = [[0]*100 for _ in range(100)]

    # 시작좌표값 구하기
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:   
                x, y = i, j

    # 반환값
    # 도달가능:1  도달 불가능: 0 


    print(f'#{test_case} {bfs(x, y)}')


