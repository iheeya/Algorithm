T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 카드의 개수
    cards = list(map(str, input().split()))
    cal = N // 2   # 카드의 개수를 반으로 나눈값
    a = []     # 카드를 반씩 잘라서 저장할 리스트
    b = []

    if N % 2 == 0:
        a = cards[:cal]
        b = cards[cal:]
    else:
        # 홀수인 카드뭉치는 앞쪽의 카드가 한장 더 갖도록 한다.
        a = cards[: cal + 1]
        b = cards[cal+1:]

    result = []   # 결과를 저장할 리스트
    result.append(a[0])   # 먼저 들어가야할 단어 append

    for i in range(1, N):
        idx = i//2     # 자른 리스트 a, b의 인덱스에 접근하기 위해 연산 필요
        if i % 2 != 0:
            result.append(b[idx])
        else:
            result.append(a[idx])

    print(f'#{test_case}', *result)