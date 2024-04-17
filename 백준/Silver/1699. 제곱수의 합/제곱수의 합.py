N = int(input())    # 제곱수의 최소 개수를 구하고자 하는 변수

# dp배열에 1의 제곱수로만 이루어져 있는 최악의 경우를 저장
# 제곱수의 수만큼 배열 생성
dp = [i for i in range(N+1)]

# 1의 제곱수는 1이므로 2부터 2의 제곱수를 구하기 시작
for i in range(2, N+1):
    # 1부터 자기자신까지 제곱
    for j in range(1, i+1):
        square = j*j    # 현재 제곱수의 값 square 변수에 저장
        if square > i:  # 만약 현재 제곱수의 값이 현재 값보다 크다면 들어갈 수 없으므로
            break       # break

        # 만약 현재 i의 제곱수의 개수가 제곱한 결과를 뺀 것 보다 크다면
        if dp[i] > dp[i-square] + 1:
            # 새로운 값으로 바꾸기
            # 이때, dp[i-square]을 통해 현재 제곱수를 뺀 값 저장. +1을 통해 현재 제곱한 제곱 수 더하기
            dp[i] = dp[i-square] + 1

print(dp[N])