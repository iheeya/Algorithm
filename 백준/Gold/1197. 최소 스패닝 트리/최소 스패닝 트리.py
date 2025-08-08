import sys
import heapq
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기 
input = sys.stdin.readline

# union 연산 함수
def union(s, e):
    fs = find(s)
    fe = find(e)
    if fs != fe:
        parent[fe] = fs   # 유니온 파인드에서는 루트끼리 연결해야 한다.

# find 연산 함수
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

V, E = map(int, input().split())
hq = []
parent = [i for i in range(V+1)]   # 각 노드의 조상을 저장할 값. (인덱스 번호 == 값으로 초기화)
result = 0   # 최소 스패닝 트리의 가중치를 저장할 변수
nNode = 0  # 에지의 개수를 카운트할 변수

# 에지 가중치, 노드 입력받기
for _ in range(E):
    a, b, c = map(int, input().split())   # 시작노드, 도착노드, 가중치
    heapq.heappush(hq, (c, a, b))    # 가중치, 시작노드, 도착노드 순으로 저장 (가중치를 기준으로 오름차순 정렬 필요)

# 가중치가 낮은 에지부터 연결
while hq:
    w, s, e = heapq.heappop(hq)   # 가중치, 시작노드, 도착 노드
    fa = find(s)
    fb = find(e)
    # 두 노드의 find 연산이 같다면 사이클이 만들어지므로 연결 x
    if fa != fb:
        result += w
        union(s, e)   # 두 노드 연결
        nNode += 1
        if nNode == V-1:
            break


print(result)




