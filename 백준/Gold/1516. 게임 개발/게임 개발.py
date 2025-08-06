from collections import deque
import sys
input = sys.stdin.readline

N = int(input())   # 건물 개수
D = [0] * (N+1)    # 진입 차수 리스트
T = [0] * (N+1)    # 건물 만드는 시간 리스트 (인덱스 = 건물 번호)
A = [[] for _ in range(N+1)]   # 인접 리스트

for i in range (1, N+1):
    B = list(map(int, input().split()))
    T[i] = B[0]
    for j in range(1, len(B)):
        if B[j] != -1:
            temp = B[j]
            A[temp].append(i)    # 인접 리스트 만들기
            D[i] += 1            # 진입차수 리스트 표기


q = deque()
result = [0] * (N+1)    # 결과 리스트

for i in range(1, N+1):
    # 진입 차수가 0인 노드를 큐에 저장
    if D[i] == 0:
        q.append(i)
        result[i] = T[i]   # 바로 지을 수 있는 건물 시간 저장


while q:
    tmp = q.popleft()

    for n in A[tmp]:
        result[n] = max(result[n], result[tmp] + T[n])  # 선행 건물 기준 최대 시간
        D[n] -= 1
        if D[n] == 0:
            q.append(n)


for i in range(1, N+1):
    print(result[i])
