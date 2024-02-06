for test_case in range(1, 11):
    tc = int(input())

    pat = input()   # 비교할 문자열 패턴 입력
    fnd = input()   # 비교대상 문자열 입력
    M = len(pat)    
    N = len(fnd)

    cnt = 0   # 일치하는 횟수를 저장할 변수

    for i in range(N-M+1):   # 원본 문자열에 패턴 문자열의 길이만큼의 길이를 남겨놓은 시작점들의 모음
        for j in range(M):   # 패턴의 길이
            if fnd[i+j] != pat[j]:    # 패턴의 길이 만큼 비교했을때 문자가 같지 않다면
                break
        else:   #같다면
            cnt += 1     # 일치 횟수 증가

    print(f'#{test_case} {cnt}')