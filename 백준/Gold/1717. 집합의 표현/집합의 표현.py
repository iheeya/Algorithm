n, m = map(int, input().split())

A = [i for i in range(n + 1)]   # 집합관계를 나타낼 리스트


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        A[rb] = ra

def find(n):
    if A[n] != n:
        A[n] = find(A[n])
    
    return A[n]

for _ in range(m):
    cal, a, b = map(int, input().split())

    # cal의 번호에 따라 다른 함수 실행
    if cal == 0:
        union(a, b)
    
    elif a == b:
        print("YES")
    
    else:
        find(a)
        find(b)
        if A[a] == A[b]:
            print("YES")
        else:
            print("NO")
