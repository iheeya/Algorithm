A = list(map(str, input().split('-')))

for i in range(len(A)):
    B = []
    if '+' in A[i]:
        B.extend(A[i].split('+'))
        B = [int(x) for x in B]
        A[i] = sum(B)


A = [int(x) for x in A]
answer = A[0]

if len(A) > 1:
    for i in range(1, len(A)):
        answer -= A[i]

print(answer)