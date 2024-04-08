from collections import deque

def bfs():
    global visited

    q = deque()
    q.append(S)
    visited[S] = 1

    while q:
        x = q.popleft()
        if x == G:
            return visited[G] - 1
    
        for nx in (x+U, x-D):
            if 1<=nx<=F and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

    return 'use the stairs'
        


F, S, G, U, D = map(int, input().split())
# F: 건물의 층수
# S: 강호가 지금 있는 층수
# G: 스타트링크가 있는 곳의 위치
# U: 위로 U층을 가는 버튼
# D: 밑으로 D층을 가는 버튼

visited = [0] * (F+1)

print(bfs())

# 출력: 버튼을 몇 번 눌러야 할까?  /  엘리베이터를 통해 갈 수 없다면 'use the staris'출력4

