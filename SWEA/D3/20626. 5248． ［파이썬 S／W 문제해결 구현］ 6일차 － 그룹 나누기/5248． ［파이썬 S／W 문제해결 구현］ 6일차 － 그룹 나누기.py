def make_set(n):
    # 각 요소가 자기 자신을 부모로 갖는 일차원 배열을 반환
    parent = [i for i in range(n + 1)]
    return parent


def find_set(x):
    # 기저조건: 자기 자신이 대표일때
    if parent[x] == x:
        return x

    # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
    parent[x] = find_set(parent[x])
    return parent[x]


def union_set(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # root_x 대표자가 root_y를 가리키게 된다.
    parent[root_x] = root_y


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N번까지의 출석 번호, M장의 강의 신청서
    nums = list(map(int, input().split()))  # M쌍의 번호

    # 출력: 몇개의 조가 만들어지는지 출력 (집합의 개수 카운트하기)
    parent = make_set(N)

    # M 쌍의 번호가 있는 nums를 활용해 집합 합치기
    for i in range(0, len(nums), 2):
        union_set(nums[i], nums[i+1])

    result = set()

    for i in range(1, N+1):    # 요소들의 길이만큼 반복
        result.add(find_set(i))   # 집합의 대표값만 저장
        # 대표값의 개수 == 집합의 개수

    print(f'#{test_case} {len(result)}')

