from collections import deque

def bfs(end):
    global visited, hq

    while hq:
        node = hq.popleft()

        if node == end:
            return visited[end]
        
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1 + visited[node]
                hq.append(next)

     
    return -1 

    


n = int(input())   # 전체 사람의 수
a, b = map(int, input().split())   # 촌수를 계산해야 하는 사람의 번호
m = int(input())   # 부모 자식들간의 관계의 개수

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for _ in range(m):
    x, y = map(int,input().split())   # 부모 자식간의 관계 / x: y의 부모 번호
    graph[x].append(y)
    graph[y].append(x)
    

hq = deque()
hq.append(a)

result = bfs(b)



# 출력: 입력에서 요구한 두 사람의 촌수를 나타내는 정수
# 촌수 관계가 없을 때는 -1 출력
if result == 0:
    print(-1)
else:
    print(result)