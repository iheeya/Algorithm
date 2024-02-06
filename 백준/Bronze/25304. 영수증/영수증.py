X = int(input())  # 영수증에 적힌 총 금액
N = int(input())  # 구매한 물건의 종류의 수
result = 0

for tc in range(N):
    a, b = map(int, input().split())    # 물건의 가격 a, 개수 b

    result += (a* b)

if X == result:
    print('Yes')
else:
    print('No')