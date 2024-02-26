T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 전선의 개수
    cnt = 0    # 교차점을 저장하기 위한 변수

    target = [list(map(int, input().split())) for _ in range(N)]
    A = []
    B = []

    for i in range(N):
        A.append(target[i][0])   # x 좌표 저장
        B.append(target[i][1])   # y 좌표 저장 

    i_A = []    # 그동안 순회한 x좌표
    i_B = []    # 그동안 순회한 y좌표

    for i in range(1, len(A)):
        i_A.append(A[i-1])
        i_B.append(B[i-1])

        for j in range(len(i_A)):
            if A[i] >= i_A[j] and B[i]<=i_B[j]:   # 전봇대 그림 그리면서 교차되는 지점 이해해보기
                cnt += 1
            elif A[i] <= i_A[j] and B[i] >= i_B[j]:
                cnt += 1


    # 출력: 전선의 교차점의 개수
    print(f'#{test_case} {cnt}')