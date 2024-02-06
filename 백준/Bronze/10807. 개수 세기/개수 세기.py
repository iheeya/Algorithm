N = int(input())

lst = list(map(int, input().split()))
fnd = int(input())

cnt = 0 # 동일한 정수가 몇개인지 카운트 하기 위한 변수

for num in lst:
    if num == fnd:
        cnt += 1

print(cnt)