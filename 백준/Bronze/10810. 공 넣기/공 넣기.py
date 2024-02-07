N, M = map(int, input().split())
# N: 바구니의 개수
# M: 앞으로 공을 넣을 횟수

# 바구니와 공의 숫자가 같아야 한다.
#이미 바구니에 공이 있다면 공을 빼고 새로 공을 넣는다.
# 공을 넣을 바구니는 연속되어 있어야 한다.

# 출력: 각 바구니에 어떤 공을 들어 있는지 (공이 없는 바구니는 0)

basket = [0] * N

for i in range(M):
    i, j, k = map(int, input().split())

    for l in range(i-1, j):
        basket[l] = k


print(*basket)