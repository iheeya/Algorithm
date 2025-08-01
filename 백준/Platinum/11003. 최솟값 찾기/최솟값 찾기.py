import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
deq = deque()

for i in range(N):
    while deq and deq[-1][1] > A[i]:
        deq.pop()
    deq.append((i, A[i]))    # deq에 [인덱스, 넘버] 순으로 저장

    # 인덱스 범위를 계산해서 슬라이딩 윈도우 범위를 넘어가면 제거
    if deq[0][0] < i-L+1:
        deq.popleft()
    
    print(deq[0][1], end = ' ')
