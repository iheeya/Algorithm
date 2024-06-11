import sys

N = int(sys.stdin.readline())
N_lst = []

for _ in range(N):
    x = int(sys.stdin.readline())
    N_lst.append(x)

N_lst.sort()

for n in N_lst:
    print(n)