import sys
input = sys.stdin.readline

N, S = map(int, input().split())  # S: 합이 되여야 할 숫자
arr = list(map(int, input().split()))
cnt = 0

# arr의 부분수열중 합이 S가 되는 부분수열의 개수를 구하라

n = len(arr)
for i in range(1, 1<< n):
    sub = []
    for j in range(n):
        if i & (1<<j):
            sub.append(arr[j])
    
    if sum(sub) == S:
        cnt += 1

print(cnt)