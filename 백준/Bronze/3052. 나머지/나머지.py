nums = []

for i in range(10):
    n = int(input())
    nums.append(n)

rest = []
for i in range(10):
    rest.append(nums[i] % 42)

cnt = 0
a = set(rest)  # 중복으로 들어간 나머지 제거

for i in range(len(a)):
    cnt += 1

print(cnt)