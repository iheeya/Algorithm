
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    multiply = []   # 입력받은 숫자들에 대한 모든 곱의 조합
    result = [-1]     # 단조 증가하는 수를 저장할 리스트 (단조증가하는 수가 없다면 -1출력)

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            multiply.append(str(A[i] * A[j]))

    # 문자열로 변환된 숫자를 순회하며 단조 증가하는 수인지 확인
    for word in multiply:
        if len(word) == 1:
            continue
        else:
            for w in range(1, len(word)):
                if word[w] < word[w-1]:
                    break
            else:
                # 단조 증가하는 수라면 result변수에 추가
                result.append(int(word))


    # 단조 증가하는 수들 중 최댓값 구하기
    mx = result[0]
    for i in range(len(result)):
        if mx < result[i]:
            mx = result[i]

    # 단조 증가하는 수들 중 최댓값 출력
    print(f'#{test_case} {mx}')


