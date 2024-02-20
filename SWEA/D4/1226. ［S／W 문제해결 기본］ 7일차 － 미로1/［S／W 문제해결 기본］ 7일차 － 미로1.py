from collections import deque

def bfs(a, b):
    global q

    q.append([a, b])  # q에 시작 좌표 넣기

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()  # q에서 현재 좌표 꺼내기

        for k in range(4):   # 갈수 있는 상하좌우 탐색
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < 16 and 0 <= ny < 16:  # 해당 좌표가 미로 안에 있고
                if maze[nx][ny] == 0:   # 갈 수 있는 길이라면
                    q.append([nx, ny])  # 현재 좌표를 q에 넣기
                    maze[x][y] = 1      # 이미 탐색한길은 더이상 탐색하지 않도록 벽으로 만들어 준다.
                if maze[nx][ny] == 3:   # 도착점이라면
                    return 1  # 1 리턴
                # 도착 가능 : 1 , 도착 불가능 : 0

    return 0


for test_case in range(1, 11):
    test_num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    q = deque()
    # 길: 0, 벽: 1, 출발: 2, 도착: 3

    # 출발 좌표 구하기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                a, b = i, j



    print(f'#{test_case} {bfs(a, b)}')
