cnt = int(input())   # N의 약수의 개수
lst = list(map(int, input().split()))  # N의 약수 리스트

lst.sort()

N = lst[0] * lst[-1]

# 출력: N
print(N)