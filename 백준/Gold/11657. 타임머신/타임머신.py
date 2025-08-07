import sys
input = sys.stdin.readline

N, M = map(int, input().split())
E = [] * (M+1)
D = [sys.maxsize] * (N+1)
D[1] = 0     # 시작노드의 가중치는 0

for _ in range(M):
    A, B, C = map(int, input().split())  # 시작 노드, 도착지 노드, 가중치(걸리는 시간)
    E.append((A, B, C))

# 가중치 구하기
for _ in range(N-1):
    for s, e, w in E:
        if D[s] != sys.maxsize and D[e] > D[s] + w:
            D[e] = D[s] + w

# 음수 사이클 확인
Cycle = False
for s, e, w in E:
    if D[s] != sys.maxsize and D[e] > D[s] + w:
        Cycle = True


# 결과 출력
for i in range(2, N+1):
    if Cycle:
        print(-1)
        break
    elif D[i] == sys.maxsize:
        print(-1)
    else:
        print(D[i])