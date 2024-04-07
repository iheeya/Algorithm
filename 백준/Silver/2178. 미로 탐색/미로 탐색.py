from collections import deque

def bfs(x, y):  
    global arr
    q = deque()
    q.append([x, y]) 
    

    arr[0][0] = 0
    
    # 사방 탐색을 위한 배열 
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 1:
                    q.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1

    return arr[N-1][M-1] + 1
                    
   


N, M = map(int, input().split())  # N: 미로의 세로 길이  M: 미로의 가로 길이 
arr = [list(map(int, input())) for _ in range(N)]  # 미로
graph = []


result = bfs(0,0)

# 출력: 도착지까지 지나야 하는 칸 수
print(result)