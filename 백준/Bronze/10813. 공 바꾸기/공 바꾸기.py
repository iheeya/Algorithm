N, M = map(int, input().split())
#N: 가지고 있는 바구니의 수
#M: 앞으로 공을 바꿀 개수
basket = [0] * N

for i in range(1, len(basket)+1):
    basket[i-1] = i

for i in range(M):
    i, j = map(int, input().split())
    # i번 바구니의 공과 j번 바구니의 공을 교환

    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]


print(*basket)
