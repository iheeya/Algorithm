import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
A = [0] * (MAX + 1)
q= deque([N])

while q:
    x = q.popleft()

    if x == K:
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and not A[nx]:   # nx를 아직 방문하지 않았을 때만 큐에 삽입
            A[nx]  = A[x] + 1
            q.append(nx)



print(A[K])
    