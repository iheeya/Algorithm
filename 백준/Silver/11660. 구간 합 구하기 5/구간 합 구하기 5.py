import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N: 배열의 크기
# M: 구간 합을 구해야 하는 횟수


# 원본 배열 A 만들기
A = [[0] * (N+1)]   # x축 첫째 줄은 모두 0으로 채우기
for _ in range(N):  # 원본 배열의 길이 만큼 반복하며 원본배열 숫자 입력받기
    row = list(map(int, input().split()))   # 각 행씩 리스트로 입력 받기
    A.append([0] + row)     # y축 첫째 줄을 0으로 채우면서 입력받은 리스트 다음 행에 추가 하기



# 합 배열 D만들기
D = [[0] * (N+1) for _ in range(N+1)]   # 모두 0으로 채워져 있는 2차원 배열 만들기
for i in range(1, N+1):   # 인덱스 i, j 계산
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]


# 구간 합 좌표 입력 받기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # 입력 받은 좌표를 사용해서 구간합 구하기
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

