N = int(input())
lst = list(map(int, input().split()))
cnt = 1    # 수열의 길이를 저장할 변수
result = 0  # 가장 긴 수열의 길이를 저장할 변수

# 커지는 수열 구하기
for i in range(1, N):
    if lst[i-1] <= lst[i]:
        cnt += 1
    else:
        if result < cnt:
            result = cnt
        cnt = 1

if result < cnt:   #끝까지 커질 수도 있으므로 따로 밖에서 조건문 실행
    result = cnt
    
cnt = 1

# 작아지는 수열 구하기
for i in range(1, N):
    if lst[i-1] >= lst[i]:
        cnt += 1
    else:
        if result < cnt:
            result = cnt
        cnt = 1
if result < cnt:
    result = cnt

print(result)
