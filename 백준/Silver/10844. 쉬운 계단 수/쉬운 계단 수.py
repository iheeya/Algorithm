import sys
input = sys.stdin.readline

N = int(input())

dp = [[0]* 10 for _ in range(N+1)]   # 자릿수x숫자개수만큼 dp배열 만들기
# dp[자릿수][해당 자리에서 가장 뒤에 오는 숫자]

for i in range(1, 10):
    dp[1][i] = 1   # 1의 자릿수의 경우 뒤에오는 숫자 = 1 ->  경우의 수 초기화


# 나머지 자릿수 탐색
for i in range(2, N+1):
    for j in range(10):
        if j == 0:   # 가장 뒤에 오는 숫자가 0이면 그 앞에는 1만 올 수 있다.
            dp[i][j] = dp[i-1][1]
        
        # 가장 뒤에 오는 숫자가 1~8일때는 +-1이 앞에 올 수 있다.
        elif 1 <= j <=8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

        # 가장 뒤에 오는 숫자가 9일때는 그 앞에 8만 올수 있다.
        else:
            dp[i][j] = dp[i-1][8]


print(sum(dp[N]) % 1000000000)