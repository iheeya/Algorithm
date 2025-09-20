import sys
input = sys.stdin.readline

def dfs(n):
    global cnt
    visited[n] = True   # 방문 처리
    cnt += 1

    for i in A[n]:
        if not visited[i]:
            dfs(i)

computer = int(input())   # 컴퓨터 개수 
connect = int(input())    # 컴퓨터 쌍 개수

A = [[] for _ in range(computer + 1)]   # 컴퓨터 쌍 저장할 인접 리스트
visited = [False] * (computer + 1)  # 방문처리를 위한 리스트
cnt = -1  # 감염된 컴퓨터 수 카운트

# 컴퓨터 순서쌍 입력
for _ in range(connect):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

dfs(1)

print(cnt)




