

T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 돌아가야 할 학생들의 수
    rooms = [list(map(int, input().split())) for _ in range(N)]   # 현재방, 돌아갈 방

    cnt = [0] * 401   # 돌아가면서 지나가는 방 번호 == 인덱스 번호. 방번호가 1-400 이므로 배열의 길이를 401까지 만든다.

    for room in rooms:
        a = room[0]   # 출발 방
        b = room[1]   # 돌아갈 방

        if a > b:   # a가 b보다 작도록 만든다.
            a, b = b, a

        # 출발지점이 짝수라면 출발지점-1 부터 이용하지 못함
        if a % 2 == 0:
            for i in range(a-1, b+1):   # range(1, 3)이라면 3은 포함하지 않으므로 계산할 값에서 +1
                cnt[i] += 1
        # 도착지점이 홀수라면 도착지점 +1까지 이용 불가능
        elif b % 2 != 0:
            for i in range(a, b+2):
                cnt[i] += 1

        else:
            for i in range(a, b+1):
                cnt[i] += 1



    print(f'#{test_case} {max(cnt)}')












