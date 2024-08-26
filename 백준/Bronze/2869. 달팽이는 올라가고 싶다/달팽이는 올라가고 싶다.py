import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

# 올라가야 할 거리 = V-B
# 하루에 갈 수 있는 거리 = A-B


if (V-B) % (A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B) + 1)
    

