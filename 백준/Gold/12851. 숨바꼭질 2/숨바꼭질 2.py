import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAX = (10 ** 5) + 1
A = [-1] * MAX
A[N] = 0
q = deque([N])
cnt = 0   # 최소 경로 개수

while q:
    x = q.popleft()

    if x == K:
        cnt += 1   
    
    for  nx in (x+1, x-1, x*2):
        if 0<= nx < MAX:
            if A[nx] == -1 :   # 처음 방문일 경우
                q.append(nx)
                A[nx] = A[x] + 1
            elif A[nx] == A[x] + 1:
                q.append(nx)

print(A[K])
print(cnt)