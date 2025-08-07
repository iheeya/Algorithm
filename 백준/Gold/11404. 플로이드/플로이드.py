import sys
input = sys.stdin.readline

n = int(input())   # 도시의 수
m = int(input())   # 버스의 수
D = [[sys.maxsize] * (n+1) for _ in range(n+1)]   # nxn 2차원 배열 만들기

# 2차원 행렬에서 두 인덱스가 같은 자리에는 0 저장 (자기자신에게 가는 경로이기 때문)
for i in range(1, n+1):
    for j in range(n+1):
        if i == j:
            D[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())    # 출발노드, 도착노드, 걸리는 시간
    if D[a][b] > c:
        D[a][b] = c   # 노드 a에서 b로 가는데 드는 돈 c


# 두 도시의 연결 비용 중 최소 값
for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            D[s][e] = min(D[s][e], D[s][k] + D[k][e])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if D[i][j] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(D[i][j], end = ' ')
    print()
