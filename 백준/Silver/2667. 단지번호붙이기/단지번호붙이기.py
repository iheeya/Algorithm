from collections import deque

def bfs(a, b, num):
    global arr
    if arr[a][b] == 0:
        return
    
    q = deque()
    q.append([a, b])

    if arr[a][b] == 1:
        arr[a][b] = num
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                arr[nx][ny] = num
                q.append([nx, ny])
    return


N = int(input())   # 배열 가로 세로 길이

arr = [list(map(int, input())) for _  in range(N)]
num = 2
s = set()


for i in range(N):
    for j in range(N):
        bfs(i, j, num)
        num += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            s.add(arr[i][j])


lst = list(s)
result = []   # 단지내 집의 수를 저장할 리스트

for l in lst:
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == l:
                cnt +=1
    result.append(cnt)

result.sort()


# 단지 개수 출력
print(len(s))
# 단지 내 집의 수를 오름 차순으로 출력
for _ in result:
    print(_)