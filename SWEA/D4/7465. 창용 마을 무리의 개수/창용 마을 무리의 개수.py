def find_set(x):
    if x == parent[x]:   #  자기자신이 대표자라면 대표자 리턴
        return x

    return find_set(parent[x])

def union_set(x, y):
    root_x = find_set(x)   # x의 대표자 찾기
    root_y = find_set(y)   # y의 대표자 찾기

    parent[root_x] = root_y   # 두 집합 합치기


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())   # N: 창용마을에 사는 사람 수  M: 서로를 알고 있는 사람의 관계 수
    parent = [i for i in range(N+1)]   # 창용마을에 사는 사람 수 만큼 대표자 리스트 만들기기

    result = set()     # 무리의 개수를 저장할 set

    for _ in range(M):
        x, y = map(int, input().split())   # 서로 알고 있는 두 사람의 번호
        union_set(x, y)   # 집합 만들기

    for group in range(1, N+1):    # 마을에 사는 사람들 만큼 반복 (1~N)
        result.add(find_set(group))     # 대표자 수 찾기

    print(f'#{test_case} {len(result)}')