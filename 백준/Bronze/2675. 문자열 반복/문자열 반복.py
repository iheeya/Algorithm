T = int(input())

for test_case in range(1, T+1):
    R, S = map(str, input().split())
    
    r = int(R)

    for i in range(len(S)):
        print(S[i] * r, end ='')
    print()