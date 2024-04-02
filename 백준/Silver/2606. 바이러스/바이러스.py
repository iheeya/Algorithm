from collections import deque

def bfs(node_num):
    global hq, visited
    
    while hq:
        node = hq.popleft()

        if visited[node] == True:
            continue
        else:
            visited[node] = True
            node_num += 1

        for next in graph[node]:        
            if not visited[next]:
                hq.append(next)
        
        

    return node_num
        



T = int(input())   # 컴퓨터의 수
N = int(input())   # 연결된 컴퓨터의 쌍 수

graph = [[] for _ in range(T+1)]
visited = [False] * (T+1)   # 방문 체크하기 위한 리스트

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

hq = deque()
hq.append(1)

result = bfs(-1)

print(result)

# 출력: 1번 컴퓨터가 바이러스가 걸렸을떄, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수


