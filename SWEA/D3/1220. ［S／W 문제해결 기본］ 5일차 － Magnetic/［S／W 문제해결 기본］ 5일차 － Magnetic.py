for test_case in range(1, 11):
    N = int(input())  # 정사각형 테이블의 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0   # 교착 상태 개수를 저장할 변수

    for i in range(100):
        is_red = False  # 빨간색이 나왔는지 안나왔는지 확인 (세로줄을 옆으로 이동할때마다 초기화되도록 한다.)
        for j in range(100):
            if arr[j][i] == 1:
                is_red = True
            elif is_red and arr[j][i] == 2:
                cnt += 1
                is_red = False    # 한번 교착상태를 카운트하고 나서는 빨간자석의 상태를 다시 False로 만든다.

    print(f'#{test_case} {cnt}')
