#계단의 개수
N = int(input())

#계단의 점수들을 scores
scores = [int(input()) for _ in range(N)]


if N == 1:
    print(scores[0])
elif N == 2:
    print(scores[0] + scores[1])
else:
    #계단 오르기 (점화식, DP)
    dp = [0] * (N+3)

    #기저조건
    dp[0] = scores[0]  # 1번째 계단을 밟을 때의 최대값
    dp[1] = scores[0] + scores[1]  #두번째 계단을 밟을 때의 최대값
    dp[2] = max(scores[1] + scores[2], scores[0] + scores[2])  # 3번째 계단을 밟을 때의 최대값

    # 점화식을 풀어서 반복으로 순회
    for x in range(3, N):
        dp[x] = max(dp[x-2] + scores[x], dp[x-3] + scores[x] + scores[x-1])

    print(dp[N-1])
