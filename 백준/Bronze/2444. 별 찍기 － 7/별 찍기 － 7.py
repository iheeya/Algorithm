user = int(input())

for i in range(1, user+1):
    print(' '*(user-i) + '*'*(2*i-1) )

for i in range(user-1, -1, -1):
    print(' '*(user-i) + '*'*(2*i-1) )