N = int(input())   # 수열의 길이
A = list(map(int, input().split()))  # 수열

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] >A[j]:
            dp[i] = max(dp[i], dp[j] + 1 )

print(max(dp))