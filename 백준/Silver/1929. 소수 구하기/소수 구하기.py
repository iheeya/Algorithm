import math, sys
input = sys.stdin.readline

M, N = map(int, input().split())

A = [i for i in range(N+1)]   # N까지의 숫자 배열 만들기
A[1] = 0    # 1은 소수가 아님을 명시

for i in range(2, int(math.sqrt(N)) + 1):
    if A[i] == 0:     # 이미 배수 처리된 수라면 스킵
        continue
    
    for j in range(i+i, N+1, i):
        A[j] = 0    # i의 배수 삭제 처리


for i in range(M, N+1):      # 범위내에서 0이 아닌수, 즉 소수인 수만 출력
    if A[i] != 0:
        print(A[i])