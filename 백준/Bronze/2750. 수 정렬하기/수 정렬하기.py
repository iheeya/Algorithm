N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

A.sort()

for a in A:
    print(a)