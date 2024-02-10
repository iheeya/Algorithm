N = int(input())

numbers = list(map(int, input()))
cnt = 0

for num in numbers:
    cnt += num

print(cnt)
