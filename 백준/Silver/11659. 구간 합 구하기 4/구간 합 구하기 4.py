import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N: 수의 개수
# M: 합을 구해야 하는 횟수

A = list(map(int, input().split()))   # 원래 배열

# 구간 합 배열 만들기
# 배열과는 달리 인덱스가 1부터 시작하므로 인덱스 0 자리에는 0 넣어 놓기

S = [0]

# 반복문을 통해 구간합 구하기
temp = 0
for n in A:
    temp += n
    S.append(temp)

for _ in range(M):
    i, j = map(int, input().split())   # 합을 구해야하는 구간 인덱스

    # 구간 합 배열을 사용해 i번째 수부터 j 번째 수의 합 구하기
    print(S[j] - S[i-1])



