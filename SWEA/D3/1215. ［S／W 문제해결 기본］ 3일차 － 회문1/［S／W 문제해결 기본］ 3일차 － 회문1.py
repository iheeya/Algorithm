for test_case in range(1, 11):

    M = int(input())    # 찾아야하는 회문의 길이
    my_str = [list(input()) for _ in range(8)]    # N : 글자판  #정확한 양식으로 입력받고 있는지 확인하자!
    N = 8    # 글자판의 가로세로 길이

    cnt = 0    #회문의 개수를 저장할 변수
    sol = []

    #가로 단어 확인
    for i in range(N):  # 모든 x 좌표 순회
        for j in range(N - M + 1):  # 시작점에서 문자길이만큼 갈 수 있을 범위
            tmp = my_str[i][j: j + M]  # 문자 길이만큼 가로 순회
            if tmp == tmp[::-1]:  # 회문이라면
                cnt += 1

        # 세로  확인단어
    for i in range(N):    # 가로세로를 한번에 확인하기 보다 안전하게 따로 확인해보자
        for j in range(N - M + 1):  # 시작점에서 문자길이만큼 갈 수 있을 범위
            tmp = []  # 알파벳을 저장할 변수
            for k in range(M):  # 문자길이
                tmp.append(my_str[j + k][i])  # 문자의 길이만큼 세로로 순회

            if tmp == tmp[::-1]:    #회문이라면
                    cnt += 1

    print(f'#{test_case} {cnt}')
