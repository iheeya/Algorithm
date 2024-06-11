N = int(input())
N_lst = []

for _ in range(N):
    x = int(input())
    N_lst.append(x)

N_lst.sort()

for n in N_lst:
    print(n)