import sys
input = sys.stdin.readline

N = int(input())   # 로프의 개수
weight = []   # 각 로프가 버틸 수 있는 중량
for _ in range(N):
    weight.append(int(input()))

weight.sort(reverse=True)
result = []

for i in range(N):
   result.append(weight[i] * (i + 1))


print(max(result))
