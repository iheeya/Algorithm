import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))    # 오리지널 배열

S = [0] * (N+1)

for i in range(N):
    S[i+1] = A[i] + S[i]


for _ in range(M):
    i, j = map(int, input().split())
    result = S[j] - S[i-1]
    print(result)

