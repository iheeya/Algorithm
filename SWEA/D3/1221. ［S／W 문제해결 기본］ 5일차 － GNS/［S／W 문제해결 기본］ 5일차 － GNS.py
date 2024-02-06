T = int(input())

for test_case in range(1, T+ 1):

    tc, N = map(str, input().split())
    N = int(N)                       # string -> int

    words = list(input().split())    # 단어 배열 입력 받기

    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']   # 숫자 단어 리스트
    result = []    # 결과를 저장할 리스트

    for i in range(10):             # 단어의 개수만큼 반복
        for j in words:             # words 배열길이만큼 반복
            if nums[i] == j:        # 숫자 단어리스트의 요소가 입력받은 리스트에 있다면
                result.append(j)    # 결과 리스트에 더하기
    # 숫자단어리스트의 처음 단어부터 비교하기 때문에 순서대로 저장된다.

    print(f'#{test_case}')
    print(*result)
