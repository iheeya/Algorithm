T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 농장의 크기
    farm = [list(map(int, input())) for _ in range(N)]   # 농작물의 가치가 저장된 리스트
    price = 0  # 농작물을 수확했을때 얻을 수 있는 이익을 저장할 값

    middle = N//2    # 중간 길이 (중간을 제외한 남은 길이 = middle * 2)
    start = middle  # 시작점 잡기
    j = 1  # 더할 길이
    # 마름모가 길이 1부터 시작해서 한칸 밑으로 올때마다 2씩 길이가 늘어난다. (중앙에서 시작)
    for i in range(start+1):
        for k in range(j):
            price += farm[i][middle+k]

        middle -= 1
        j += 2      # col의 인덱스 값이 middle일때 까지 2씩 늘어나고

    j -= 2    # 위에서 한번 더 계산한 j값과 인덱스 값을 가운데 줄에 밑으로 오도록 한번 더 추가 계산
    middle += 1

    # middle 인덱스를 넘어가게 된다면 2씩 감소한다.
    for i in range(start+1, N):
        # 마지막줄에 올때 까지 반복
        j -= 2
        middle += 1
        for k in range(j):
            price += farm[i][middle + k]


    print(f'#{test_case} {price}')
