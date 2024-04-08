from collections import deque

def bfs(N, K):
    global visited
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        # 현재 방문 노드가 동생의 위치와 같다면
        if x == K:
            print(visited[x])
            break
        
        for nx in (x+1, x-1, x*2):
            if 0<=nx<=100000 and not visited[nx]:
                visited[nx] = visited[x]+1
                q.append(nx)



N, K = map(int, input().split())
# N: 수빈이의 위치
# K: 동생의 위치

visited = [0] *100001

bfs(N, K)

# 출력: 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
