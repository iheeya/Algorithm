N = int(input())   # 카드의 개수
lst = [0] + list(map(int, input().split()))    # 카드의 가격 (인덱스를 맞추기 위해 앞에 0추가)
dp = [0] * (N+1)

dp[1] = lst[1]
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j] + lst[j] , dp[i])

# 출력: N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최대값
print(dp[N])