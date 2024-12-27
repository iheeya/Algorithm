N = int(input())  # 주어진 자연수

result = 0

for num in range(1, (N+1)):
    result += (N//num) * num

print(result)