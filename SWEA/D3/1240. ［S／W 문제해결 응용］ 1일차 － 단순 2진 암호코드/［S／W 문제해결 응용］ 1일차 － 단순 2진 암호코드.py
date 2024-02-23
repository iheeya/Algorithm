
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N: 세로길이, M: 가로길이
    arr = [list(map(int, input())) for _ in range(N)]

    # 암호코드에서 숫자 하나는 7개의 비트로 암호화되어 이루어진다.
    convert = {
        '3211': 0,
        '2221': 1,
        '2122': 2,
        '1411': 3,
        '1132': 4,
        '1231': 5,
        '1114': 6,
        '1312': 7,
        '1213': 8,
        '3112': 9
    }

    bn = []  # 7개의 이진수를 결과를 저장할 리스트(2차원 배열)
    tmp = []  # 56개 숫자를 저장할 리스트
    change = []   # 이진수를 10진수로 바꾼 결과를 저장할 리스트
    password = []   # 4씩 암호를 잘라서 한자리 숫자로 바꾼 결과를 저장할 리스트

    # 7씩 자르면 되는게 아니라
    # 가로길이가 56이 되도록 주어진 가로 길이에서 필요 없는 0의 개수를 쳐내야한다.
    # 뒤에서부터 순환하면서 1이 나오면 그 순간부터 56개 자르기
    # 56개를 자른 결과에서 다시 7씩 나누어서 bn에 저장
    for j in range(N):  # 세로길이
        for i in range(M-1, 0, -1):  #가로길이
            if arr[j][i] == 1:
                for k in range(56):
                    tmp.append(arr[j][i - k])
                break

    # # 거꾸로 저장된 이진수들을 다시 reverse()
    a = list(reversed(tmp))
    # bn리스트에 7개씩 잘라서 넣기
    for i in range(0, len(a), 7):
        bn.append(a[i:i+7])

    # bn리스트의 비율을 파악해서 10진수로 변환
    for b in bn:
        cnt = 1
        for i in range(6):  # 마지막 비트는 따로 처리
            if b[i] == b[i + 1]:
                cnt += 1
            else:
                change.append(cnt)
                cnt = 1

            # 마지막 비트 처리
        if b[6] == 0:
            cnt += 1
        else:
            change.append(cnt)

    # 4개씩 잘라서 convert 딕셔너리를 통해 1의자리숫자로 전환
    for i in range(0, len(change), 4):
        z = change[i: i+4]
        result_string = ''.join(map(str, z))
        password.append(convert[result_string])

    # 한줄에 8개의 숫자가 존재
    # 암호코드: (홀수 자리의 합 * 3) + (짝수 자리의 합) == 10의 배수
    # 10의 배수라면 암호코드에 포함된 숫자의 합 출력, 배수가 아니라면 0 출력
    sum = 0
    for p in range(0, len(password), 8):
        even = 0
        odd = 0
        r = password[p:p+8]   # 숫자 8개를 저장한 리스트 r
        for i in range(len(r)):
            if i % 2 == 0:
                even += r[i]
            else:
                odd += r[i]

        calc = ((even * 3) + odd) % 10
        if calc == 0:
            sum = even + odd
        else:
            sum = 0

    print(f'#{test_case} {sum}')



# 출력: 올바른 암호코드: 암호코드에 포함된 숫자의 합, 잘못된 암호코드 : 0
