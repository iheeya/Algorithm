n = int(input())
lst = list(map(int, input().split()))


dp = [0 for _ in range(n)]
dp[0] = lst[0]

for i in range(1, n):
    # 연속합이 더 큰지, 연속합 보다 현재 리스트의 값이 더 큰지 확인
    dp[i] = max(dp[i-1] + lst[i], lst[i])

print(max(dp))

