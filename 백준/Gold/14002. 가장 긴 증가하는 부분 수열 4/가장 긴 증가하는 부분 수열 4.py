N = int(input())   # 수열의 길이
A = list(map(int, input().split()))  # 수열
result = []

dp = [1 for _ in range(N)]
result.append(A[0])

for i in range(1, N):
    for j in range(i):
        if A[i] >A[j]:
            dp[i] = max(dp[i], dp[j] + 1 )

max_length = max(dp)           

result = []
for i in range(N-1, -1, -1):
    if dp[i] == max_length:
        result.append(A[i])
        max_length -= 1

result.reverse()

print(len(result))
print(*result)