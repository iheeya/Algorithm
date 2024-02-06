T = int(input())

for test_case in range(1, T+ 1):

    tc, N = map(str, input().split())
    N = int(N)

    words = list(input().split())

    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    result = []

    for i in range(10):
        for j in words:
            if nums[i] == j:
                result.append(j)

    print(f'#{test_case}')
    print(*result)
