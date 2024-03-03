N = int(input())
lst = list(map(int, input().split()))
inc_cnt = 1  # 증가하는 수열의 길이를 저장할 변수
dec_cnt = 1  # 감소하는 수열의 길이를 저장할 변수
result = 1   # 가장 긴 수열의 길이를 저장할 변수 (최소값은 1)

for i in range(1, N):
    if lst[i-1] <= lst[i]:
        inc_cnt += 1
    else:
        inc_cnt = 1  # 증가하는 수열이 끊겼을 때 초기화

    if lst[i-1] >= lst[i]:
        dec_cnt += 1
    else:
        dec_cnt = 1  # 감소하는 수열이 끊겼을 때 초기화

    result = max(result, inc_cnt, dec_cnt)

print(result)
