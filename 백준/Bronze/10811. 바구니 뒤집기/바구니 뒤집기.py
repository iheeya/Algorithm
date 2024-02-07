N, M = map(int, input().split())
# N: 바구니의 개수

basket = [0] * N

for i in range(N):
    basket[i] = i+1    # 바구니에 1부터 순차대로 번호 부여


for r in range(M):
    i, j = map(int, input().split())
    #i, j : 역순의 범위

    tmp = basket[i-1:j]  # 역순의 범위만큼 잘라 임시저장
    tmp.reverse()        # 역순 만들기
    basket[i-1:j] = tmp    #만든 역순을 원래 리스트에 저장


print(*basket)