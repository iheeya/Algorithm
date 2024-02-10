dial = ['ABC', 'DEF', 'GHI','JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0 # 걸리는 시간을 계산할 변수

word = input()

for i in word:
    for j in range(len(dial)):
        if i in dial[j]:
            time += j + 3

print(time)