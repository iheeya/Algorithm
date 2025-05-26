import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N: 배열의 크기 M: 나누어 떨어져야 하는 수
A = list(map(int, input().split()))   # 원본 배열
answer = 0   # 정답(구간의 개수)을 저장할 변수

# 합 배열 구하기
S = [0] * N
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

# 나머지가 같은 수들을 저장할 리스트 (나머지=인덱스, 나머지가 같으면 인덱스의 요소 증가)
C = [0] * M

# 합 배열 S의 원소들을 M으로 나누어 저장
for i in range(N):
    remain = S[i] % M
    if remain == 0:
        answer +=1
    C[remain] += 1

# 나머지가 같은 인덱스 중 2개를 골라 그 사이의 합 배열을 계산하면 나머지가 0
for i in range(M):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1)) // 2

print(answer)



