n1, n2 = input().split()

s1 = int(n1[::-1])
s2 = int(n2[::-1])


if s1>s2:
    print(s1)
else:
    print(s2)
