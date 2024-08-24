import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
cnt = 0

for _ in range(N):
    c = int(input())
    if c > K:
        continue
    else:
        coins.append(c)

coins.sort(reverse=True)

for coin in coins:
    cnt += K//coin
    K %= coin


print(cnt)
