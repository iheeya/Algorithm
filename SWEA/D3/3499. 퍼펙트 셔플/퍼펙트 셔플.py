def get_result():
    # 투포인트 알고리즘에서 point1 = 맨 처음, point2 = 중간 +1
    pointer1 = 0
    pointer2 = (N + 1) // 2

    for turn in range(N):
        if turn % 2 == 0:
            print(str[pointer1], end=' ')
            pointer1 += 1
        else:
            print(str[pointer2], end=' ')
            pointer2 += 1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 카드의 개수
    str = list(input().split())

    print(f'#{test_case}', end = ' ')
    get_result()
    print()   # 케이스가 출력될때마다 줄바꿈
